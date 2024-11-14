from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.BigIntegerField( 
        validators=[ 
            MinValueValidator(1000000000),
            MaxValueValidator(9999999999),
        ],
        unique=True,
        null=True,
        blank=True
    )

    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=150, unique=True, default='default_user')

    def __str__(self):
        return str(self.phone_number)
