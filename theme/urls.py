
# File: theme/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Route for the homepage
    path('', views.home, name='home'),
    
    # NEW: Route for the research page
    path('research/', views.research_discussion, name='research'),
]