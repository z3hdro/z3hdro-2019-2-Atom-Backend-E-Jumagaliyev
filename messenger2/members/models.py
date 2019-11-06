from django.db import models
from chats.models import Chat
from message.models import Message
from django.conf import settings

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True, verbose_name='Диалог')
    new_messages = models.TextField('Новые сообщения')
    last_read_message = models.OneToOneField(Message, on_delete=models.SET_NULL, null=True, verbose_name='Последнее прочитанное сообщение')

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участиники'