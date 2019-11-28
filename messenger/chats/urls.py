from django.urls import path
from chats.views import create_chat, show_all_chats, show_special_chat

urlpatterns = [
    path('createchat/', create_chat, name='create_chat'),
    path('showchats/', show_all_chats, name='show_all_chats'),
    path('showchat/', show_special_chat, name='show_special_chat')
]