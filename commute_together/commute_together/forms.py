from django.forms import ModelForm

from commute_together.models import MeetingModel

class MeetingForm(ModelForm):
	class Meta:
		model = MeetingModel
		fields = ['name', 'date', 'desc', 'place']
