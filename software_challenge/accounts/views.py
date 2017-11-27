from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

from . import forms
from accounts.models import LoginInstance, LogoutInstance

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'


class MyLoginView(LoginView):

    def post(request):
        login = LoginInstance.objects.create(user=request.user)
        login.save()
        return super().post(request)


class MyLogoutView(LogoutView):

    def post(request):
        logout = LogoutInstance.objects.create(user=request.user)
        logout.save()
        return super().post(request)
