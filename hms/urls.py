from django.urls import path
from django.conf.urls import *

from . import views

urlpatterns = [
    path('', views.emp_login, name='login'),
    url(r'^HomePage$', views.HomePage, name='HomePage'),
    url(r'^Register_Doctor$', views.Register_Doctor, name='Register_Doctor'),
    url(r'^register_opeartion$', views.register_operation, name='register_operation'),
    url(r'^register_testing$', views.register_testing, name='register_testing'),
    url(r'^register_prescription$', views.register_prescription, name='register_prescription')
]
