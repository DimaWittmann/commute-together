from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.timezone import localtime

# Create your models here.
class MeetingModel(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=255)
	date = models.DateTimeField()
	desc = models.TextField()
	place = models.CharField(max_length=80)

	def get_absolute_url(self):
		return reverse('meeting', args=[self.id])

	def serialize(self):
		result = {}
		result['author_id'] = self.user.id
		result['author_first_name'] = self.user.first_name
		result['author_last_name'] = self.user.last_name
		result['author_photo'] = self.user.vkuser.photo
		result['id'] = self.id
		result['title'] = self.name
		result['date'] = localtime(self.date).strftime('%d-%m-%Y %H:%M')
		result['desc'] = self.desc
		result['place'] = self.place
		return result

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