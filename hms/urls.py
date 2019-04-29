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

    url(r'^Register_Recep$', views.Register_Recep, name='Register_Recep'),
    url(r'^Get_Employee_Info$', views.Get_Employee_Info, name='Get_Employee_Info'),
    url(r'^Update_Employee_Info$', views.Update_Employee_Info, name='Update_Employee_Info'),

    url(r'^Create_Room$', views.Create_Room, name='Create_Room'),
    url(r'^Insert_Operation$', views.Insert_Operation, name='Insert_Operation'),
    url(r'^Insert_Medicine$', views.Insert_Medicine, name='Insert_Medicine'),
    url(r'^Insert_Test$', views.Insert_Test, name='Insert_Test'),
    url(r'^Get_Room_Info$', views.Get_Room_Info, name='Get_Room_Info'),
    url(r'^Update_Room_Info$', views.Update_Room_Info, name='Update_Room_Info'),
    url(r'^Get_Medical_Info$', views.Get_Medical_Info, name='Get_Medical_Info'),
    url(r'^Update_Medical_Info$', views.Update_Medical_Info, name='Update_Medical_Info'),

]
