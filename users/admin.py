""" Admin de Usuarios."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from users.models import User


class CustomeUserAdmin(UserAdmin):
    """Admistrador del modelo de User"""
    list_display=('email','username','picture','first_name','last_name','is_staff','is_client')
    list_display_links=('email',)
    list_editable=('picture',)
    list_filter=('is_client','is_staff','created','modified')

admin.site.register(User,CustomeUserAdmin)