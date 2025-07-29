# File: theme/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Route for the homepage
    path('', views.home, name='home'),
    
    # Route for the research page
    path('research/', views.research_discussion, name='research'),

    # NEW: Route for the about page
    path('about/', views.about, name='about'),

    # NEW: Route for the discussion page
    path('discussion/', views.discussion, name='discussion'),

    # NEW: Route for exploring topics
    path('explore-topics/', views.explore_topics, name='explore_topics'),

    # NEW: Route for the login page
    path('login/', views.login_view, name='login'),

    # NEW: Route for the user profile page
    path('profile/', views.profile, name='profile'),
]