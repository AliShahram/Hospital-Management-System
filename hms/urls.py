from django.urls import path
from django.conf.urls import *

from . import views

urlpatterns = [
    path('', views.emp_login, name='login'),
    url(r'^HomePage$', views.HomePage, name='HomePage'),
    url(r'^Admin_Staff$', views.Admin_Staff, name='Admin_Staff'),
    url(r'^Admin_Medicine$', views.Admin_Medicine, name='Admin_Medicine'),
    url(r'^Admin_Logistics$', views.Admin_Logistics, name='Admin_Logistics'),
]
