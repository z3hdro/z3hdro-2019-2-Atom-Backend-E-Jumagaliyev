from django.urls import path
from users.views import find_user, create_user, show_all_users

urlpatterns = [
    path('finduser/<str:username>/', find_user, name='find_user'),
    path('createuser/', create_user, name='create_user'),
    path('showusers/', show_all_users, name='show_all_users')
]