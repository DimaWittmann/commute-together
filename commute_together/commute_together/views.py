from django.shortcuts import render, redirect, get_object_or_404

from commute_together.forms import MeetingForm
from commute_together.models import MeetingModel

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
	else:
		form = MeetingForm()
		return render(request, 'new_meeting.html', {'form': form})


def meeting(request, meeting_id):
	meeting = get_object_or_404(MeetingModel, pk=meeting_id)
	return render(request, 'meeting.html', {'meeting': meeting})