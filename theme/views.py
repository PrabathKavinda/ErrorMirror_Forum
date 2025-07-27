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


