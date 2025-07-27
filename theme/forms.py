from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# We are extending Django's built-in UserCreationForm to add custom styling
# and potentially more fields later.
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email') # You can add 'first_name', 'last_name' if you want

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom CSS classes to the form fields for styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-full px-6 py-3 rounded-xl bg-gray-800/70 border border-gray-700 focus:outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 transition-all'
            field.widget.attrs['placeholder'] = field.label