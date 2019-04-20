from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .SQL_Queries import *

# Create your views here.

db = Database()

def emp_login(request):
    return render(request, 'hms/login.html')

def HomePage(request):
    e_id = request.GET.get('e_id')
    employee_type = db.ident_employee_type(e_id)

    #print(employee_type[0])
    if employee_type:
        if employee_type == 'd':
            return render(request, 'hms/doctor.html')
        elif employee_type == 'r':
            return render(request, 'hms/receptionist/receptionist_table_choice.html')
        elif employee_type == 'a':
            return render(request, 'hms/admin.html')
    else:
        context = {'emp':e_id}
        return render(request, 'hms/login.html', context )

def receptionist_table_choice(request):
    return render(request, 'hms/receptionist/table_choice.html')

def ReceptionistTableChoice(request):
    table = request.GET.get('choice')
    if table == "Patitent":
        return render(request, 'hms/receptionist/receptionist_patient.html')
    elif table == "Visit":
        return render(request, 'hms/receptionist/receptionist_visit.html')
    elif table == "Admission":
        return render(request, 'hms/receptionist/receptionist_admission.html')
    elif table == "Appointment":
        return render(request, 'hms/receptionist/receptionist_appointment.html')
    else:
        return render(request, 'hms/receptionist/receptionist_patient.html')
        

# def UpdatePatient(request):
#     p_id = request.Get.get("p_id")
#     return render(request, 'hms/receptionist/receptionist_update_patient.html')
