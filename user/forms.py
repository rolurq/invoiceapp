from django.contrib.auth.forms import UserCreationForm

from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        exclude = ('is_superuser', 'groups', 'user_permissions', 'is_staff', 'is_active', 'date_joined', 'last_login')