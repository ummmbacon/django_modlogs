# modlogs/urls.py
from django.urls import path

from .views import Home, SearchResultsListView
from . import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('r/<subreddit>/', views.index, name='index',),
    path('r/<subreddit>/search', SearchResultsListView.as_view(), name="search_results"),
]



