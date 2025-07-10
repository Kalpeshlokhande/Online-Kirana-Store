from django.contrib import admin
from apps.users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'name', 'phone', 'is_admin', 'is_staff')
    search_fields = ('email', 'username', 'name', 'phone')