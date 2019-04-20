from django.urls import path
from django.conf.urls import *

from . import views

urlpatterns = [
    path('', views.emp_login, name='login'),
    url(r'^HomePage$', views.HomePage, name='HomePage'),
    url(r'^Register_Doctor$', views.Register_Doctor, name='Register_Doctor'),
    url('operate', views.operate, name='Operate_Procedure'),
    url('prescribe', views.prescribe, name='Prescribe_medicine'),
    url('test', views.test, name='Conduct_Test')
]
