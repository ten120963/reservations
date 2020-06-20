from django.urls import path
from . import views
#from .views import ByDateView, SearchResultsView
from .views import SearchResultsView

urlpatterns = [
	path('', views.home, name="home"),  
	path('add/', views.add, name="add"),  
	path('edit/<list_id>', views.edit, name="edit"),   
	path('delete/<list_id>', views.delete, name="delete"), 	
	path('by_date/', views.by_date, name="by_date"), 	
	path('list_all/', views.list_all, name="list_all"), 
	path('search/', SearchResultsView.as_view(), name='search_results'),
    #path('by_date/', ByDateView.as_view(), name='by_date'),	
]
