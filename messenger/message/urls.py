from django.urls import path
from message.views import create_message, show_all_messages

urlpatterns = [
    path('createmessage/', create_message, name='create_message'),
    path('showmessages/', show_all_messages, name='show_all_messages')
]