from django.urls import path
from chats.views import create_chat, show_all_chats

urlpatterns = [
    path('createchat/', create_chat, name='create_chat'),
    path('showchats/', show_all_chats, name='show_all_chats')
]