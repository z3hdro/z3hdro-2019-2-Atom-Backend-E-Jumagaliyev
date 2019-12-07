from django.contrib import admin
from users.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'email', 'last_login', 'is_superuser',  'avatar')

admin.site.register(User, UserAdmin)