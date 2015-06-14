from django.test import LiveServerTestCase
from selenium import webdriver


class MainPageTestCase(LiveServerTestCase):
	def setUp(self):
		self.selenium = webdriver.Firefox()


	def tearDown(self):
		self.selenium.quit()


	def test_new_meeting_addition(self):

		# User opens main page
		self.selenium.get('%s%s' % (self.live_server_url, '/meeting/'))

		# User tries adding new appointment(name, description and date)
		self.selenium.find_element_by_xpath('//input[@value="New appointment"]').click()

		name = 'New meeting'
		date = '01.01.2001 08:13'
		desc = 'Looking for company on mornign train'
		place = 'Klavdieve station'
		name_input = self.selenium.find_element_by_id('id_name')
		name_input.send_keys(name)
		date_input = self.selenium.find_element_by_id('id_date')
		date_input.send_keys(date)
		desc_input = self.selenium.find_element_by_id('id_desc')
		desc_input.send_keys(desc)
		place_input = self.selenium.find_element_by_id('id_place')
		place_input.send_keys(place)

		self.selenium.find_element_by_xpath('//input[@value="Add appointment"]').click()


		# User sees appointment page and see all info and plays to add comment
		self.assertRegex(self.selenium.current_url, '/meeting/\d+')
		page_text = self.selenium.find_element_by_tag_name('body').text
		self.assertIn(name, page_text)
		self.assertIn(date, page_text)
		self.assertIn(place, page_text)



		# New user connected
		self.selenium.quit()
		self.selenium = webdriver.Firefox()

		# new user sees main page
		self.selenium.get('%s%s' % (self.live_server_url, '/meeting/'))
		page_text = self.selenium.find_element_by_tag_name('body').text
		self.assertIn(name, page_text)
		self.assertIn(date, page_text)

		# he open the same appoitment and see all information and comment

		self.selenium.get('%s%s%d' % (self.live_server_url, '/meeting/', 1))
		page_text = self.selenium.find_element_by_tag_name('body').text
		self.assertIn(name, page_text)
		self.assertIn(date, page_text)
		self.assertIn(desc, page_text)
		self.assertIn(place, page_text)
		
		# Both users leave the page.
		self.selenium.quit()


