from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.
class MeetingModel(models.Model):
	name = models.CharField(max_length=255)
	date = models.DateTimeField()
	desc = models.TextField()
	place = models.CharField(max_length=80)

	def get_absolute_url(self):
		return reverse('meeting', args=[self.id])

	class Meta:
		ordering = ('date', )


class StationModel(models.Model):
	name = models.CharField(max_length=40, unique=True)
	code = models.CharField(max_length=40)


class CommentModel(models.Model):
	author_name = models.CharField(max_length=80)
	comment = models.CharField(max_length=255)
	meeting = models.ForeignKey(MeetingModel)
	timestamp = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-timestamp',)


class VkUser(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	access_token = models.CharField(max_length=255)
	vkuser_id = models.IntegerField()
	photo = models.CharField(max_length=255)