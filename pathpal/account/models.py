from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=150, unique=True, default='default_user', verbose_name='phone number')

    def __str__(self):
        return str(self.username)
