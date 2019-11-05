from django.db import models
from django.contrib.auth.models import AbstractUser
from chat.models import Chat, Message

# Create your models here.
class User(AbstractUser):
    avatar = models.CharField('Аватар', max_length = 120, blank=True)

class Member(models.Model):
    #user = models.OneToOneField()
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    new_messages = models.TextField()
    last_read_message = models.OneToOneField(Message, on_delete=models.SET_NULL, null=True)