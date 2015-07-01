import json
import urllib
import re
from datetime import datetime, date

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils.timezone import localtime
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


from commute_together.forms import MeetingForm, CommentForm
from commute_together.models import MeetingModel, StationModel, CommentModel
from commute_together.settings import VK_APP_ID, VK_API_SECRET, LOGIN_URL, DATETIME_FORMAT
import commute_together.utils as utils



# Create your views here.

def home(request):
	form = MeetingForm()
	logged = request.user.is_authenticated()
	return render(request, 'home.html', {'login_url': LOGIN_URL, 'logged_in': logged, 'DATETIME_FORMAT': DATETIME_FORMAT})


@login_required
def new_meeting(request):

	if request.method == 'POST':
		form = MeetingForm(request.POST)
		if form.is_valid():
			user = User.objects.get(id=request.user.id)
			new_meeting = form.save(user)
			return redirect(new_meeting)

	elif request.method == 'GET':
		appointment = datetime.now()

		t = request.GET.get('date', None)
		if t:
			t = datetime.strptime(t, '%H:%M:%S')
			appointment = datetime.combine( date.today(), t.time())

		form = MeetingForm(initial={
			'place': request.GET.get('place', ''),
			'date': appointment.strftime('%d.%m.%Y %H:%M'),
			'name': request.GET.get('name', '')
			})

	return render(request, 'new_meeting.html', {'form': form, 'DATETIME_FORMAT': DATETIME_FORMAT})


def vklogin(request):

	if request.method == 'GET':
		code = request.GET.get('code', None)
		if code:
			params = {
				'client_id': VK_APP_ID,
				'client_secret': VK_API_SECRET,
				'code': code,
				 'redirect_uri': 'http://dimawittmann.pythonanywhere.com/meeting/vklogin'
			}
			url = 'https://oauth.vk.com/access_token'
			json_response = utils.get_json(url, params)

			user = authenticate(user_info = json_response)
			if user:
				login(request, user)
				messages.info(request, 'Hello ' + user.first_name + ' ' + user.last_name)
			else:
				messages.error(request, 'Error during authentication')
		else:
			messages.error(request, request.GET.get('error', ''))
			messages.error(request, request.GET.get('error_description', ''))

		return redirect('home')


def logout_view(request):
	#messages.info(request, 'Bye ' + request.user.first_name + ' ' + request.user.last_name)

	logout(request)
	return redirect('home')


def meeting(request, meeting_id):
	form = CommentForm()
	meeting = get_object_or_404(MeetingModel, pk=meeting_id)
	return render(request, 'meeting.html', {'meeting': meeting, 'form': form, 'VK_APP_ID': VK_APP_ID, 'DATETIME_FORMAT': DATETIME_FORMAT})


def schedule(request):
	return render(request, 'schedule.html')


def get_schedule_JSON(request):

	if request.method == 'GET':
		from_station = request.GET.get('from')
		to_station = request.GET.get('to')

		board = utils.get_threads_between_stations(from_station, to_station)

	return JsonResponse(board, safe=False)


def station_name_hints_JSON(request):
	if request.method == 'GET':
		value = request.GET['query']

		query = StationModel.objects.filter(name__startswith=value)
		suggestions = [{'value': station.name, 'data': station.name} for station in query]

		return JsonResponse({'suggestions' :suggestions}, safe=False)

def get_board_JSON(request):
	if request.method == 'GET':
		date = request.GET.get('date', None)
		station = request.GET.get('from_station', '')
		only_friends = request.GET.get('friends', None) #is equal 1 the True
		page = request.GET.get('page', 1)

		qs = MeetingModel.objects

		if date:
			date = datetime.strptime(date, '%d.%m.%Y %H:%M')   # is it required?
			qs = qs.filter(date__gte=date)
		else:
			qs = qs.filter(date__gte=datetime.now())

		if station:
			qs = qs.filter(place=station) 

		if only_friends:
			friends = utils.get_user_friends(request.user.id)
			qs.filter(user__vkuser__vkuser_id__in=friends)

		records = qs.all()
		p = Paginator(records, 20)

		return JsonResponse(list(map(lambda x: x.serialize(), p.page(page).object_list)), safe=False)
