from django import forms

from commute_together.models import MeetingModel, CommentModel

class MeetingForm(forms.models.ModelForm):
	
	class Meta:
		model = MeetingModel
		fields = ['name', 'date', 'desc', 'place']


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
