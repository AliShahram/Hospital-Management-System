from django.urls import path
from django.conf.urls import *

from . import views

urlpatterns = [
    path('', views.emp_login, name='login'),
    url(r'^HomePage$', views.HomePage, name='HomePage'),
    url(r'^Register_Doctor$', views.Register_Doctor, name='Register_Doctor'),
    url(r'^Register_Recep$', views.Register_Recep, name='Register_Recep'),
    url(r'^Get_Employee_Info$', views.Get_Employee_Info, name='Get_Employee_Info'),
    url(r'^Update_Employee_Info$', views.Update_Employee_Info, name='Update_Employee_Info'),
]
