# File: theme/views.py

from django.shortcuts import render

# This view renders your homepage
def home(request):
    return render(request, 'home.html')

# NEW: This view will render your new research page
def research_discussion(request):
    return render(request, 'research.html')

# --- --- --- --- --- --- --- --- --- --- --- --- ---

