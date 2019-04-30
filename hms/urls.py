from django.urls import path
from django.conf.urls import *

from . import views

urlpatterns = [
    path('', views.emp_login, name='login'),
    url(r'^HomePage$', views.HomePage, name='HomePage'),
    url(r'^Register_Doctor$', views.Register_Doctor, name='Register_Doctor'),
    url(r'^register_operation$', views.register_operation, name='register_operation'),
    url(r'^register_testing$', views.register_testing, name='register_testing'),
    url(r'^DoctorHomePage$', views.DoctorHomePage, name='DoctorHomePage'),
    url(r'^register_prescription$', views.register_prescription, name='register_prescription'),
    url(r'^get_medical_history$', views.get_medical_history, name='get_medical_history')
]
