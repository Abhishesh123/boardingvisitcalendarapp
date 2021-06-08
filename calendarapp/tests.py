from django.test import TestCase
from django.template.defaultfilters import slugify
from calendarapp.models import Event


class EventModelsTestCase(TestCase):
    def test_event_has_slug(self):
        """Posts are given slugs correctly when saving"""
        event = Event.objects.create(first_name=" Abhishesh")
        post.save()
        self.assertEqual(event.slug, slugify(event.first_name))