from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_location/', views.add_location, name='add_location'),
    path('locations/', views.location_view, name='locations'),
]

