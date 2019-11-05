from chat_list.views import chat_lists, contacts
from django.urls import path

urlpatterns = [
        path('chatlist/', chat_lists, name='chat_lists'),
        path('contacts/', contacts, name='contacts')
]