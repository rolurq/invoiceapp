from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login

login_forbidden = user_passes_test(lambda u: u.is_anonymous, '/')

from .models import User
from .forms import SignUpForm

class SignUpView(generic.CreateView):
    model = User
    exclude = ('is_superuser', 'groups', 'user_permissions', 'is_staff', 'is_active', 'date_joined', 'last_login')
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = '/'

    @method_decorator(login_forbidden)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
