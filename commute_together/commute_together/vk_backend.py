from django.conf import settings
from django.contrib.auth.models import User


from commute_together.models import VkUser
from commute_together.utils import get_json

class VkBackend(object):


	def authenticate(self, user_info):
		try:
			user = User.objects.get(email=user_info['email'])
		except User.DoesNotExist:
			user = User(email=user_info['email'])
			user.save()
			vkuser = VkUser(user=user,
				access_token=user_info['access_token'], vkuser_id=user_info['user_id'])
			vkuser.save()

			params ={
				'user_ids': vkuser.vkuser_id,
				'fields': 'photo_50'
			}

			url = 'https://api.vk.com/method/users.get'

			response = get_json(url, params)['response'][0]

			user.first_name = response['first_name']
			user.last_name = response['last_name']
			user.vkuser.photo = response['photo_50']
			user.vkuser.save()
			user.save()

		return user


	def get_user(self, id):
		try:
			return User.objects.get(pk=id)
		except User.DoesNotExist:
			return None