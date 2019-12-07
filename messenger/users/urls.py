from django.urls import path
from users.views import show_all_users, update_data_on_user, find_user, find_my_id

urlpatterns = [
    path('finduser/', find_user, name='find_user'),
    path('showusers/', show_all_users, name='show_all_users'),
    path('findme/', find_my_id, name='find_my_id'),
    path('updateuser/', update_data_on_user, name='update_data_on_user')
]