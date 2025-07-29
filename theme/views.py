# File: theme/views.py


from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm # Import the new form
from django.contrib import messages


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

def register(request):
    if request.method == 'POST':
        # If the form has been submitted, process the data
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('home') # Redirect to the homepage after successful registration
    else:
        # If it's a GET request, just display a blank registration form
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


