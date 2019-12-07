from django.db import models
from users.models import User
from chats.models import Chat 


# Create your models here.
class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True, verbose_name='Диалог')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    content = models.TextField('Содержимое')
    added_at = models.DateTimeField('Дата и время добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
