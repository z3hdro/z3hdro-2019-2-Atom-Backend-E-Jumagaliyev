from django.urls import path
from chats.views import create_chat, show_all_chats, show_special_chat

urlpatterns = [
    path('createchat/', create_chat, name='create_chat'),
    path('showchat/', show_special_chat, name='show_special_chat'),
    path('showchats/', show_all_chats, name='show_all_chats')
]

#     

# from chats.views import ChatViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', ChatViewSet, basename='chats')
# urlpatterns = router.urls