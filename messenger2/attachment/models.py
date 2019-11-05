from django.db import models
from chats.models import Chat
from message.models import Message
from django.conf import settings

# Create your models here.
class Attachment(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True, verbose_name='Диалог')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True, verbose_name='Сообщение')
    type_attachment = models.CharField('Тип Прикрепления',max_length=12)
    url = models.CharField('Ссылка',max_length=200)