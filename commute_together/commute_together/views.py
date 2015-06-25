import json
import urllib
import re
from datetime import datetime, date

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils.timezone import localtime


from commute_together.forms import MeetingForm, CommentForm
from commute_together.models import MeetingModel, StationModel, CommentModel
from commute_together.settings import VK_APP_ID, VK_API_SECRET
import commute_together.utils as utils



# Create your views here.



def home(request):
	form = MeetingForm()
	appointments = MeetingModel.objects.order_by('date').all().reverse()
	return render(request, 'home.html', {'appointments': appointments, 'client_id': VK_APP_ID})


def new_meeting(request):
	
	if request.method == 'POST':
		form = MeetingForm(request.POST)
		if form.is_valid():
			new_meeting = form.save()
			return redirect(new_meeting)

	elif request.method == 'GET':
		appointment = datetime.now()

		t = request.GET.get('date', None)
		if t:
			t = datetime.strptime(t, '%H:%M:%S')
			appointment = datetime.combine( date.today(), t.time())

		form = MeetingForm(initial={
			'place': request.GET.get('place', ''),
			'date': appointment.strftime('%Y-%m-%d %H:%M'),
			'name': request.GET.get('name', '')
			})

	return render(request, 'new_meeting.html', {'form': form})


def vklogin(request):
	if request.method == 'GET':
		code = request.GET.get('code', None)
		if code:
			params = {
				'client_id': VK_APP_ID,
				'client_secret': VK_API_SECRET,
				'code': code,
				'redirect_uri': 'dimawittmann.pythonanywhere.com/meeting/vklogin'
			}
			url = 'https://oauth.vk.com/access_token'
			json_response = utils.get_json(url, params)
			return JsonResponse(json_response)
		else:
			print (request.GET.get('error'), '')
			print (request.GET.get('error_description'), '')

def meeting(request, meeting_id):
	form = CommentForm()
	meeting = get_object_or_404(MeetingModel, pk=meeting_id)
	return render(request, 'meeting.html', {'meeting': meeting, 'form': form})


def schedule(request):
	return render(request, 'schedule.html')

def get_schedule(request):

	if request.method == 'GET':
		from_station = request.GET.get('from')
		to_station = request.GET.get('to')

		board = utils.get_threads_between_stations(from_station, to_station)

	return JsonResponse(board, safe=False)



def station_name_hints(request):
	if request.method == 'GET':
		value = request.GET['query']

		query = StationModel.objects.filter(name__startswith=value)
		suggestions = [{'value': station.name, 'data': station.name} for station in query]

		return JsonResponse({'suggestions' :suggestions}, safe=False)


def add_comment(request):
	if request.method == 'POST':
		meeting_id = request.POST.get('meeting_id')
		author_name = request.POST.get('author_name')
		comment = request.POST.get('comment')

		meeting = get_object_or_404(MeetingModel, pk=meeting_id)

		comm = CommentModel(author_name=author_name, comment=comment, meeting=meeting)		

		comm.save()

		response = {}
		response['author_name'] = author_name
		response['comment'] = comment
		response['date'] = localtime(comm.timestamp).strftime('%B %d, %Y %I:%M %p')

		return JsonResponse(response, safe=False)