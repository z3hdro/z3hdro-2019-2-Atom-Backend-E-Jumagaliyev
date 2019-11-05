from chats.views import render_method
from django.urls import path

urlpatterns = [
        path('', render_method, name='render_method'),
]
