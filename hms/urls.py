from django.urls import path
from django.conf.urls import *

from . import views

urlpatterns = [
    path('', views.emp_login, name='login'),
    url(r'^HomePage$', views.HomePage, name='HomePage'),
    path('', views.receptionist_table_choice, name='receptionist_table_choice'),
    url(r'^ReceptionistTableChoice$', views.ReceptionistTableChoice, name='ReceptionistTableChoice'),
]
