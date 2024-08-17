
from django.urls import path
from Users.views import BirthdayListView, BirthdayCreateView


urlpatterns = [
    path('home/', BirthdayListView.as_view(), name='home'),
    path('add/', BirthdayCreateView.as_view(), name='add_birthday'),
]
