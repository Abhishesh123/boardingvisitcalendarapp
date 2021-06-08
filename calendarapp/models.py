from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200, unique=True, null=True)
    last_name = models.CharField(max_length=200, unique=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.first_name
    
    def get_absolute_url(self):
        return reverse('calendarapp:event-detail', args=(self.id,))

    @property
    def get_html_url(self):

        data=Event.objects.all()
        # print(data)

        l=data.filter(start_time__date=self.start_time).count()
        date = data.filter(start_time__date=self.start_time)
        print(self.start_time)
        url = reverse('calendarapp:event-detail', args=(self.start_time.day,))
        return f'<a href="{url}"> {l} </a>'


class EventMember(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['event', 'user']

    def __str__(self):
        return str(self.user)