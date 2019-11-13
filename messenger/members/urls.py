from django.urls import path
from members.views import create_member, show_all_members

urlpatterns = [
    path('createmember/', create_member, name='create_member'),
    path('showmembers/', show_all_members, name='show_all_members')
]