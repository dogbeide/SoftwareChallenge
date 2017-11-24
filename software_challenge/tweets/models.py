from django.db import models

# Create your models here.
class Tweet(models.Model):
    handle = models.CharField(max_length=128)
    text = models.CharField(max_length=140)

    def __str__(self):
        self.handle
