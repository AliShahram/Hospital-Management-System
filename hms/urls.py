from django.urls import path
from django.conf.urls import *

from . import views

urlpatterns = [
    path('', views.emp_login, name='login'),
    url(r'^HomePage$', views.HomePage, name='HomePage'),
    url(r'^Admin_Staff$', views.Admin_Staff, name='Admin_Staff'),
    url(r'^Admin_Medicine$', views.Admin_Medicine, name='Admin_Medicine'),
    url(r'^Admin_Logistics$', views.Admin_Logistics, name='Admin_Logistics'),
    url(r'^Register_Doctor$', views.Register_Doctor, name='Register_Doctor'),
    url(r'^Create_Room$', views.Create_Room, name='Create_Room'),
    url(r'^Insert_Operation$', views.Insert_Operation, name='Insert_Operation'),
    url(r'^Insert_Medicine$', views.Insert_Medicine, name='Insert_Medicine'),
    url(r'^Insert_Test$', views.Insert_Test, name='Insert_Test'),
]
