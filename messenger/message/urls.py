from django.urls import path
from message.views import create_message, show_all_messages, read_message

urlpatterns = [
    path('createmessage/', create_message, name='create_message'),
    path('readmessage/', read_message, name='read_message'),
    path('showmessages/', show_all_messages, name='show_all_messages')
]