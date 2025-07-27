# File: theme/urls.py - THIS IS CORRECT

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('research/', views.research_discussion, name='research'),
    path('register/', views.register, name='register'),
]