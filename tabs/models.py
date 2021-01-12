from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #additional
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

class Song(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    name = models.CharField(max_length = 20)
    key = models.CharField(max_length = 2)

    def __str__(self):
        return self.name

class Notes(models.Model):
    upper_octave = models.BooleanField(default = False)
    comment = models.CharField(max_length = 50)
    hole_1 = models.BooleanField(default = False)
    hole_2 = models.BooleanField(default = False)
    hole_3 = models.BooleanField(default = False)
    hole_4 = models.BooleanField(default = False)
    hole_5 = models.BooleanField(default = False)
    hole_6 = models.BooleanField(default = False)
    song = models.ForeignKey(Song, on_delete = models.SET_NULL, null=True)


    def __str__(self):
        return str(self.id)


