from django.urls import path
from django.conf.urls import *

from . import views

urlpatterns = [
    path('', views.emp_login, name='login'),
    url(r'^HomePage$', views.HomePage, name='HomePage'),
    path('', views.receptionist_table_choice, name='receptionist_table_choice'),
    url(r'^ReceptionistTableChoice$', views.ReceptionistTableChoice, name='ReceptionistTableChoice'),
    url(r'^Patient$', views.Patient, name='Patient'),
    url(r'^RegisterPatient$', views.Register_Patient, name='RegisterPatient'),
    url(r'^UpdatePatient$', views.Update_Patient, name='UpdatePatient'),
    url(r'^Get_Patient_Info$', views.Get_Patient_Info, name='Get_Patient_Info'),
    url(r'^Visit$', views.Visit, name='Visit'),
    url(r'^Get_Visit_Info$', views.Get_Visit_Info, name='Get_Visit_Info'),
    url(r'^CreateVisit', views.Create_Visit, name='CreateVisit'),
    url(r'^Update_Visit$', views.Update_Visit, name='Update_Visit'),
    url(r'^Get_Admission_Info$', views.Get_Admission_Info, name='Get_Admission_Info'),
    url(r'^Create_Admission', views.Create_Admission, name='Create_Admission'),
    url(r'^Update_Admission', views.Update_Admission, name='Update_Admission'),
    url(r'^Appointment$', views.Appointment, name='Appointment'),
    url(r'^Get_Appointment_Info$', views.Get_Appointment_Info, name='Get_Appointment_Info'),
    url(r'^Create_Appointment,', views.Create_Appointment, name='Create_Appointment'),
    url(r'^Update_Appointment', views.Update_Appointment, name='Update_Appointment'),
    url(r'^Consultation$', views.Consultation, name='Consultation'),
    url(r'^Admission$', views.Admission, name='Admission'),
]
