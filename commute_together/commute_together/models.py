from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class MeetingModel(models.Model):
	name = models.CharField(max_length=40)
	date = models.CharField(max_length=40)
	desc = models.TextField()
	place = models.CharField(max_length=80)

	def get_absolute_url(self):
		return reverse('meeting', args=[self.id])
