from django.contrib import admin
from django.urls import path, include # <-- The fix is here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theme.urls')),
]