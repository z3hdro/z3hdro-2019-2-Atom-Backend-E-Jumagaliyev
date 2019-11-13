from django.contrib import admin
from chats.models import Chat
# Register your models here.

class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_group_chat', 'topic', 'last_message')

admin.site.register(Chat, ChatAdmin)