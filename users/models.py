from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.core.validators import RegexValidator, MinValueValidator,MaxValueValidator
from datetime import date, timedelta

from rest_framework import viewsets


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


USER = "user"
ADMIN = "admin"

ROLES = [
    (USER, USER),
    (ADMIN, ADMIN),
]
phone_reg = RegexValidator(
    regex=r'^(\+?7|8)(\d{10})$',

    message="Номер телефона должен быть в формате: '+71234567890'. "
)



class User(AbstractUser):
    objects = CustomUserManager()
    username= None
    full_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(max_length=254, unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



