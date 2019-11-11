from django.urls import path
from users.views import find_user

urlpatterns = [
    path('finduser/<str:username>/', find_user, name='find_user')
]