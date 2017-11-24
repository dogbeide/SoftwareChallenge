from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
