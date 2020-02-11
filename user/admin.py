from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User

admin.site.register(User)

class PublicAdmin(AdminSite):
    login_form = AuthenticationForm

    def has_permission(self, request):
        return request.user.is_active

public_admin = PublicAdmin(name='publicadmin')

class UserAdmin(admin.ModelAdmin):
    exclude = ('password', 'is_superuser', 'groups', 'user_permissions', 'is_staff', 'is_active', 'date_joined', 'last_login')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(pk=request.user.pk)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return request.user == obj

    def has_delete_permission(self, request, obj=None):
        return False

    def has_module_permission(self, request):
        return True

public_admin.register(User, UserAdmin)
