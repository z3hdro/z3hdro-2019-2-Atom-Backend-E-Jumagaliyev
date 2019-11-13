from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    avatar = models.CharField('img', null=True, max_length=32)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


