from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm

from project.store.models import *


class UserAdminChangeForm(UserChangeForm):
    """
    handle the admin dashboard list fields
    """
    class Meta(UserChangeForm.Meta):
        model = User


class UserAdmin(BaseUserAdmin):
    model = User
    ordering = ['id']
    form = UserAdminChangeForm
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_active')
        
    fieldsets = (
        (None, {
            'fields': ('email', 'first_name','password',
            'last_name', 'is_admin',
            'is_active', 'is_staff', 'is_superuser')
            }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_admin',
            'is_active', 'is_staff', 'is_superuser', 'first_name',
            'last_name'),
        }),
    )

    search_fields = ('first_name', 'last_name', 'email')

    list_filter = ('is_active',)