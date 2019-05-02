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

    url(r'^register_operation$', views.register_operation, name='register_operation'),
    url(r'^register_testing$', views.register_testing, name='register_testing'),
    url(r'^DoctorHomePage$', views.DoctorHomePage, name='DoctorHomePage'),
    url(r'^register_prescription$', views.register_prescription, name='register_prescription'),
    url(r'^get_medical_history$', views.get_medical_history, name='get_medical_history'),
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
    url(r'^Get_Consultation_Info$', views.Get_Consultation_Info, name='Get_Consultation_Info'),
    url(r'^Create_Consultation,', views.Create_Consultation, name='Create_Consultation'),
    url(r'^Update_Consultation_Info', views.Update_Consultation_Info, name='Update_Consultation_Info'),
    url(r'^Consultation$', views.Consultation, name='Consultation'),
    url(r'^Admission$', views.Admission, name='Admission'),
]
