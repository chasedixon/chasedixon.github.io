from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(default='profile_pictures/icon-profile.jpg', upload_to='profile_pictures', verbose_name='Profile Picture')
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    bio = models.TextField(max_length=255, null=True)

    def __str__(self):
        return self.user.username


class FollowUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follow = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' -> ' + self.follow.user.username
