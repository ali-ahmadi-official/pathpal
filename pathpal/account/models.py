from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, phone_number, full_name, password=None, **extra_fields):
        """
        Create and return a regular user with phone_number and full_name.
        """
        if not phone_number:
            raise ValueError('The Phone number must be set')
        user = self.model(phone_number=phone_number, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, full_name, password=None, **extra_fields):
        """
        Create and return a superuser with phone_number and full_name.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, full_name, password, **extra_fields)


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

    full_name = models.CharField(max_length=255, blank=False, default='user')

    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)

    USERNAME_FIELD = 'phone_number'
    
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return str(self.phone_number)
