from datetime import timedelta, datetime

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from commute_together.models import MeetingModel, StationModel


class HomePageTest(TestCase):
	fixtures = ['StationModel.json']

	def test_home_page_renders_template(self):
		response = self.client.get(reverse('home'))
		self.assertTemplateUsed(response, 'home.html')

