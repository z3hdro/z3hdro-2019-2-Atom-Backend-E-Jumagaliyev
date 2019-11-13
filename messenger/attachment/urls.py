from django.urls import path
from attachment.views import create_attachment, show_all_attachments

urlpatterns = [
    path('createattachment/', create_attachment, name='create_attachment'),
    path('showattachemnts/', show_all_attachments, name='show_all_attachments')
]