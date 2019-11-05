from user_profile.views import profile, page
from django.urls import path

urlpatterns = [
        path('profile/', profile, name='user_profile'),
        path('page/', page, name='page')
]