from django.urls import path
from message.views import create_message, show_all_messages, show_all_group_messages

urlpatterns = [
    path('createmessage/', create_message, name='create_message'),
    path('showgroupmessages/', show_all_group_messages, name='show_all_group_messages'),
    path('showmessages/', show_all_messages, name='show_all_messages')
]

# from message.views import MessageViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', MessageViewSet, basename='message')
# urlpatterns = router.urls