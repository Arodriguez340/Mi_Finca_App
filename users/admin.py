from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {'fields': ('role', 'phone', 'fincaName')}),
    )
    list_display = ['username', 'email', 'firstName', 'lastName', 'role', 'is_staff']