from django.shortcuts import render
from chats.models import Chat

# Create your views here.
def Find_User(request, username):
    username = str(username)
    return Chat.objects.filter(id = username)