from django.test import TestCase
from commute_together.models import MeetingModel

class MeetingModelTest(TestCase):


	def test_saving_and_retrieving_items(self):

		item = MeetingModel()
		item.name = "Meeting"
		item.date = "11.11.2011"
		item.desc = "description!"
		item.save()

		item = MeetingModel()
		item.name = "new Meeting"
		item.date = "11.11.2011"
		item.desc = "new description!"
		item.save()

		saved_items = MeetingModel.objects.all()
		self.assertEqual(saved_items.count(), 2) 

		self.assertEqual(saved_items[0].name, "Meeting")

	def test_get_absolute_url(self):
		meeting = MeetingModel.objects.create()
		self.assertEqual(meeting.get_absolute_url(), '/meeting/%d/' % (meeting.id, ))