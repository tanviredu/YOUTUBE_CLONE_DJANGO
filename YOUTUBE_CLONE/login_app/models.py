from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ''' Describe the Profile Model here '''
    user            = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    profile_picture = models.ImageField(upload_to="display_pictures",blank=True)
    about           = models.CharField(blank=True,max_length=100)
    full_name       = models.CharField(max_length=255,blank=True)
    website         = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
        
         
