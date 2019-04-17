from django.urls import path
from django.conf.urls import *

from . import views

urlpatterns = [
    path('', views.emp_login, name='login'),
    url(r'^HomePage$', views.HomePage, name='HomePage'),
]
