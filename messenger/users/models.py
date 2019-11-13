from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    avatar = models.CharField('аватар', null=True, default='None', max_length=32, blank=True)
    bio = models.TextField('биография', default='empty', max_length=250, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


