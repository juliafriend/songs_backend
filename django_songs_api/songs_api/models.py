from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=32)
    artist = models.CharField(max_length=32)
    image = models.CharField(max_length=60)
    listened_to = models.BooleanField(null = True)