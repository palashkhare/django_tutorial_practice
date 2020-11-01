from django.db import models

# Create your models here.

class contact_me(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    mobile = models.CharField(max_length = 15)
    reason_description = models.TextField()
    address = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
    

# Django has User model to save user details like username, password, email
# This user class (or any class) can be extended by adding one to one relationship
# to this class. Following is where we will extend the built in user model
        
from django.contrib.auth.models import User

# Create extended model here
class UserProfileExtention(models.Model):
    
    # Create relationship with Users model. DONT INHERIT!
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    # Add additional attributes
    portfolio_site = models.URLField(blank=True)
    
    # To handle Images, python needs its native library 'pillow'
    picture = models.ImageField(upload_to = 'profile_pix', blank=True)
    
    def __str__(self):
        # Built in attribute of django.contrib.auth.models.User
        return self.user.username