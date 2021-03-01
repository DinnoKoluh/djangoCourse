from django.db import models
import PIL # importing the pillow package

from django.contrib.auth.models import User # importing the predefined User model from djanog (inside the admin page where we have User and Group)
# Create your models here.

class UserProfileInfo(models.Model):
    # adding additional info to the User class (which it does not have) (they already have some basic info like: username, pass, email, f_name, l_name)
    # we don't inherit the User class directly, it may screw up the database (for whatever reason)
    user = models.OneToOneField(User, on_delete=models.CASCADE) 

    # aditional classes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)

    def __str__(self):
        return self.user.username

