from django.test import LiveServerTestCase
from selenium import webdriver


class MainPageTestCase(LiveServerTestCase):
	def setUp(self):
		self.selenium = webdriver.Firefox()


	def tearDown(self):
		self.selenium.quit()


	def test_new_meeting_addition(self):

		# User opens main page
		# provided place for new meating name, time and description


		# User tries adding new appointment(name description and time)

		# User sees showed new appointment info


		# User open appointment page and see all info and plays to add comment

		# User add comment


		# New user connected
		# he open the same appoitment and see all iformation and comment

		# new user create another comment

		# The user reload page and see the second comment

		# Both users leave the page.


