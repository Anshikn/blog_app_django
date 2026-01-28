from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm
# Create your views here.

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'auth/registration.html'

# class LoginView(CreateView):
#     form_class = AuthenticationForm
#     success_url = reverse_lazy('blog_index')
#     template_name = 'auth/login.html'