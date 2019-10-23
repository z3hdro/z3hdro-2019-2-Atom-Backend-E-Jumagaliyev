from chats.views import render_method, user_profile
from django.urls import path

urlpatterns = [
        path('<int:pk>', render_method, name='render_method'),
        path('id=<int:id>', user_profile, name='user_profile'),
]
