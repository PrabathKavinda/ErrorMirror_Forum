# File: theme/views.py

from django.shortcuts import render

# This view renders your homepage
def home(request):
    return render(request, 'home.html')

# NEW: This view will render your new research page
def research_discussion(request):
    return render(request, 'research.html')

# NEW: View for the about page
def about(request):
    return render(request, 'about.html')

# NEW: View for the discussion page
def discussion(request):
    return render(request, 'discussion.html')

# NEW: View for exploring topics
def explore_topics(request):
    return render(request, 'explore-topics.html')

# NEW: View for the login page
def login_view(request):
    return render(request, 'login.html')

# NEW: View for the user profile page
def profile(request):
    return render(request, 'profile.html')

# --- --- --- --- --- --- --- --- --- --- --- --- ---

