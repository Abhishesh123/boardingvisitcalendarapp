from django.urls import path

from . import views

app_name = 'calendarapp'
urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.create_event, name='event_new'),
    path('event/edit/<int:pk>/', views.EventEdit.as_view(), name='event_edit'),
    path('event/<int:day>/details/', views.event_details, name='event-detail'),
    path('event/<int:pk>/remove', views.EventMemberDeleteView.as_view(), name="remove_event"),
]