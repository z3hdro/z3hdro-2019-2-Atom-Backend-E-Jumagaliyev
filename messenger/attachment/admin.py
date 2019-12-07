from django.contrib import admin
from attachment.models import Attachment
# Register your models here.

class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat', 'user', 'message', 'type_attachment', 'url')

admin.site.register(Attachment, AttachmentAdmin)