from django.contrib import admin
from members.models import Member
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'chat', 'new_messages', 'last_read_message')

admin.site.register(Member, MemberAdmin)