from django.db import models

# Create your models here.
class Chat(models.Model):
    is_group_chat = models.BooleanField('Групповой чат')
    topic = models.CharField('Заголовок',max_length=64)
    last_message = models.TextField('Последнее сообщение')

    class Meta:
        verbose_name = 'Диалог'
        verbose_name_plural = 'Диалоги'