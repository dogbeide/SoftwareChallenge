from django.db import models
from django.contrib import auth


class User(auth.models.AbstractUser):

    def __str__(self):
        return self.username
