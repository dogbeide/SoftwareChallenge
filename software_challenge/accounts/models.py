from django.db import models
from django.contrib import auth
from django.contrib.postgres.fields import JSONField


class User(auth.models.AbstractUser):

    def __str__(self):
        return self.username


class LoginInstance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_history')
    date = models.DateTimeField(auto_now_add=False)


class LogoutInstance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logout_history')
    date = models.DateTimeField(auto_now_add=False)
