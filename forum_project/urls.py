# File: forum_project/urls.py - MAKE SURE IT LOOKS LIKE THIS

from django.contrib import admin
from django.urls import path, include # Make sure 'include' is here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theme.urls')), # This line points to your other urls.py file
]