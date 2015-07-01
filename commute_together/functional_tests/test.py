from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


class MainPageTestCase(LiveServerTestCase):
	fixtures = ['StationModel.json']

	def setUp(self):
		self.selenium = webdriver.Firefox()


	def tearDown(self):
		self.selenium.quit()


	def test_schedule_view(self):

		# User opens main page
		self.selenium.get('%s%s' % (self.live_server_url, '/meeting/'))

		# User tries adding new appointment(name, description and date)
		self.selenium.find_element_by_partial_link_text('Suburban').click()
		self.selenium.implicitly_wait(1)

		from_station = 'Клавдиево'
		to_station = 'Святошин'


		from_input = self.selenium.find_element_by_id('id_from')
		from_input.send_keys(from_station)
		to_input = self.selenium.find_element_by_id('id_to')
		to_input.send_keys(to_station)
		from_input = self.selenium.find_element_by_id('id_from')

		

