from django.urls import path
from attachment.views import create_attachment

urlpatterns = [
    path('createattachment/', create_attachment, name='create_attachment')
]