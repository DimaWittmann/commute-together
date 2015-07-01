from django.test import TestCase
from commute_together.models import MeetingModel

class MeetingModelTest(TestCase):


	def test_saving_and_retrieving_items(self):

		item = MeetingModel()
		item.name = "Meeting"
		item.date = "2011-11-11 11:11"
		item.desc = "description!"
		item.place = "Station"
		item.save()

		item = MeetingModel()
		item.name = "new Meeting"
		item.date = "2011-11-11 11:11"
		item.desc = "new description!"
		item.place = "Station"
		item.save()

		saved_items = MeetingModel.objects.all()
		self.assertEqual(saved_items.count(), 2) 

		self.assertEqual(saved_items[0].name, "Meeting")

	def test_get_absolute_url(self):
		meeting = MeetingModel.objects.create()
		self.assertEqual(meeting.get_absolute_url(), '/meeting/%d/' % (meeting.id, ))
