from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    avatar = models.CharField(max_length=200, default='avatar/AvatarNone.png')
    bio = models.TextField('биография', default='empty', max_length=250, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


