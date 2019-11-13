from django.urls import path
from chats.views import create_chat, show_all

urlpatterns = [
    path('createchat/<int:is_group_chat>/<str:topic>/<str:last_message>/', create_chat, name='create_chat'),
    path('showchats/', show_all, name='show_all')
]