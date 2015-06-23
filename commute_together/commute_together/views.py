import json
import urllib
import re
from datetime import datetime, date


from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from commute_together.forms import MeetingForm
from commute_together.models import MeetingModel, StationModel
import commute_together.utils as utils

# Create your views here.



def home(request):
	form = MeetingForm()
	appointments = MeetingModel.objects.all()
	return render(request, 'home.html', {'appointments': appointments})


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


def meeting(request, meeting_id):
	meeting = get_object_or_404(MeetingModel, pk=meeting_id)
	return render(request, 'meeting.html', {'meeting': meeting})


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


