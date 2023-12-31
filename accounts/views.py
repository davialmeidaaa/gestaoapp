from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')

class UserLogoutView(LogoutView):
    next_page = '/' 

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
