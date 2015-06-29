from django import forms

from commute_together.models import MeetingModel, CommentModel
from commute_together.settings import DATETIME_FORMAT

class MeetingForm(forms.models.ModelForm):
	
	class Meta:
		model = MeetingModel
		fields = ['name', 'date', 'desc', 'place']

		widgets = {
			'name': forms.widgets.TextInput(
				attrs={'required': True, }
			),
			'date': forms.widgets.DateTimeInput(
				attrs={'required': True, 'autocomplete': 'off'}, 
				format=DATETIME_FORMAT
			),
			'desc': forms.widgets.DateTimeInput(
				attrs={'required': True}
			),
			'place': forms.widgets.DateTimeInput(
				attrs={'required': True}
			),
		}

	def save(self, user):
		self.instance.user = user
		return super().save()


class CommentForm(forms.models.ModelForm):
	
	class Meta:
		model = CommentModel
		fields = ['author_name', 'comment']

		widgets = {
			'author_name': forms.widgets.TextInput(
				attrs={'id': 'id_author_name', 'required':True, 'placeholder': 'Input your name'}
			),
			'comment': forms.widgets.Textarea(
				attrs={'id': 'id_comment', 'required': True, 'placeholder': 'Say somethin...', 'rows': 3}
			),
		}
