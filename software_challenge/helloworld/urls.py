from django.conf.urls import url
from . import views

app_name = 'helloworld'

urlpatterns = [
    url(r'^$', views.HelloWorld.as_view(), name='index'),
]
