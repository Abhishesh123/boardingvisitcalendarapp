from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from calendarapp.models import Event

class EventModelTEst(TestCase):

    def create_event_model_test(self, first_name="german", last_name="shepherd",start_time="2021-06-10 23:23:00",end_time="2021-07-10 23:23:00"):
        return Event.objects.create(first_name=first_name, last_name=last_name,start_time=start_time,end_time=end_time, created_date=timezone.now())

    def test_event_model_creation(self):
        w = self.create_event_model_test()
        self.assertTrue(isinstance(w, Event))
        self.assertEqual(w.__unicode__(), w.first_name)



    def test_event_list_view(self):
        w = self.create_event_model_test()
        url = reverse("calendarapp.views.EventEdit")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.title, resp.content)