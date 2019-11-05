from django.db import models

# Create your models here.
class Chat(models.Model):
    is_group_chat = models.BooleanField()
    topic = models.CharField(max_length=64)
    last_message = models.TextField()

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    added_at = models.DateField()

class Attachment(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    #user = models.
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)
    type_attachment = models.CharField(max_length=12)
    url = models.CharField(max_length=200)