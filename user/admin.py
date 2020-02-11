from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User

admin.site.register(User)

# class UserAdminAuthenticationForm(AuthenticationForm):
#     """
#     Same as Django's AdminAuthenticationForm but allows to login
#     any user who is not staff.
#     """
#     this_is_the_login_form = forms.BooleanField(widget=forms.HiddenInput,
#                                 initial=1,
#                                 error_messages={'required': ugettext_lazy(
#                                 "Please log in again, because your session has"
#                                 " expired.")})

#     def clean(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#         message = ERROR_MESSAGE

#         if username and password:
#             self.user_cache = authenticate(username=username, password=password)
#             if self.user_cache is None:
#                 if u'@' in username:
#                     # Mistakenly entered e-mail address instead of username?
#                     # Look it up.
#                     try:
#                         user = User.objects.get(email=username)
#                     except (User.DoesNotExist, User.MultipleObjectsReturned):
#                         # Nothing to do here, moving along.
#                         pass
#                     else:
#                         if user.check_password(password):
#                             message = _("Your e-mail address is not your "
#                                         "username."
#                                         " Try '%s' instead.") % user.username
#                 raise forms.ValidationError(message)
#             # Removed check for is_staff here!
#             elif not self.user_cache.is_active:
#                 raise forms.ValidationError(message)
#         self.check_for_test_cookie()
#         return self.cleaned_data

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
