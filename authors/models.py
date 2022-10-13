from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    pic = models.URLField(default="https://i.imgur.com/a3vO917.jpg", blank=False)
    bio = models.CharField(max_length=400)
    twitter = models.CharField(max_length=40, blank=True)
    youtube = models.CharField(max_length=40, blank=True)
    facebook = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.name

