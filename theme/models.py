from django.db import models
from django.contrib.auth.models import User

# ==============================================================================
# 1. Profile Model
# This extends Django's built-in User model to add an avatar and bio.
# ==============================================================================
class Profile(models.Model):
    # This creates a one-to-one link to a User account.
    # If a User is deleted, their Profile is deleted too (on_delete=models.CASCADE).
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # NOTE: You will need to install the Pillow library for ImageField to work.
    # In your terminal, run: pip install Pillow
    from django.templatetags.static import static
    import os
    
    def get_default_avatar():
        default_path = static('images/default_avatar.jpg')
        if not os.path.exists(default_path):
            raise FileNotFoundError(f"Default avatar file not found at {default_path}")
        return default_path
    
    avatar = models.ImageField(default=get_default_avatar, upload_to='profile_avatars')
    bio = models.TextField(max_length=500, blank=True, null=True)

    # This is how the object will be displayed in the Django admin panel.
    def __str__(self):
        return f'{self.user.username} Profile'

# ==============================================================================
# 2. Category Model
# This model stores the main forum categories like "Development".
# ==============================================================================
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500)
    
    # This fixes the plural name in the Django admin panel (e.g., "Categorys" -> "Categories")
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

# ==============================================================================
# 3. Thread Model
# This represents a single discussion topic within a Category.
# ==============================================================================
class Thread(models.Model):
    title = models.CharField(max_length=200)
    
    # A thread must belong to a Category. This is a many-to-one relationship.
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    # A thread is started by a User.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # These timestamps are set automatically by Django.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # Tracks the last reply time

    def __str__(self):
        return self.title

# ==============================================================================
# 4. Post Model
# This represents a single reply within a Thread.
# ==============================================================================
class Post(models.Model):
    # A post must be part of a Thread.
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    
    # A post is written by a User.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reply by {self.author.username} in "{self.thread.title}"'

