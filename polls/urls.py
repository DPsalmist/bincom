from django.urls import path
from .views import HomeView, SearchResultsView
from . import views

urlpatterns = [
	path('', views.HomeView.as_view(), name='index'),
	path('create_poll/', views.createPoll, name='create'),
	path('total_results/', views.totalResults, name='total_results'),
	path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
