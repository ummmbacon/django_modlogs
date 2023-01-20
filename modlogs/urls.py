# modlogs/urls.py
from django.urls import path

from .views import Home
from . import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('r/<subreddit>/', views.index, name='index',),
]



