from django.db import models
from chats.models import Chat
from django.conf import settings

# Create your models here.
class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True, verbose_name='Диалог')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    content = models.TextField('Содержимое')
    added_at = models.DateField('Время добавления')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'