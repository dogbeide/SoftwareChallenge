from django.conf.urls import url
from django.urls import reverse_lazy
# from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from . import views

app_name = 'accounts'

urlpatterns = [

    url(r'login/$',
        views.MyLoginView.as_view(template_name='accounts/login.html'),
        name='login'),
    url(r'logout/$',
        views.MyLogoutView.as_view(),
        name='logout'),
    url(r'signup/$',
        views.SignUpView.as_view(),
        name='signup'),
    url(r'password-change/$',
        PasswordChangeView.as_view(template_name='accounts/password_change_form.html', success_url='accounts/password-change/done'),
        name='password_change'),
    url(r'password-change/done/$',
        PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
        name='password_change_done'),
    url(r'password-reset/$',
        PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
        name='password_reset'),
    url(r'^password-reset/done/$',
        PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/done/$',
        PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),
]









#
