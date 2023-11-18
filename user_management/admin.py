from django.contrib import admin

from user_management.models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_customer', 'is_delivery_agent', 'is_active', 'is_staff', 'is_superuser', 'is_blocked')
    list_filter = ('is_customer', 'is_delivery_agent', 'is_active', 'is_staff', 'is_superuser', 'is_blocked')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_customer', 'is_delivery_agent', 'is_blocked')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_customer', 'is_delivery_agent')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()  # Remove the problematic references

admin.site.register(CustomUser, CustomUserAdmin)