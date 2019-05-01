from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .Execute_SQL_Queries import *
from django.views.decorators.csrf import csrf_protect
# Create your views here.

db = Database()


def emp_login(request):
    return render(request, 'hms/login.html')

def Admin_Staff(request):
    return render(request, 'hms/admin_staff.html')

def Admin_Medicine(request):
    return render(request, 'hms/admin_medicine.html')

def Admin_Logistics(request):
    return render(request, 'hms/admin_logistics.html')

def HomePage(request):
    e_id = request.GET.get('e_id')
    employee_type = db.ident_employee_type(e_id)
    employee_type="r"
    if employee_type:
        if employee_type == 'd':
            return render(request, 'hms/doctor.html')
        elif employee_type == 'r':
            return render(request, 'hms/receptionist/receptionist_patient.html')
        elif employee_type == 'a':
            return render(request, 'hms/admin_staff.html')
    else:
        context = {'emp':e_id}
        return render(request, 'hms/login.html', context )

def receptionist_table_choice(request):
    return render(request, 'hms/receptionist/table_choice.html')

def ReceptionistTableChoice(request):
    table = request.GET.get('choice')
    if table == "Patient":
        return render(request, 'hms/receptionist/receptionist_patient.html')
    elif table == "Visit":
        return render(request, 'hms/receptionist/receptionist_visit.html')
    elif table == "Admission":
        return render(request, 'hms/receptionist/receptionist_admission.html')
    elif table == "Appointment":
        return render(request, 'hms/receptionist/receptionist_appointment.html')
    elif table == "Consultation":
        return render(request, 'hms/receptionist/receptionist_consultation.html')

def receptionist_patient(request):
    return render(request, 'hms/receptionist/receptionist_patient.html')

def Register_Patient(request):
    if request.POST:
        result = db.register_patient(request.POST)
        message = result
    else:
        message = None
    context = {'message':message}
    return render(request, 'hms/receptionist/receptionist_patient.html', context)


def Get_Patient_Info(request):
    if request.POST:
        querySet, message = db.get_patient_info(request.POST)
    context = {'querySet':querySet, 'message':message}
    return render(request, 'hms/receptionist/receptionist_patient.html', context)

def Update_Patient(request):
    if request.POST:
        print("post received")
        if 'Update' in request.POST:
            message = db.update_patient_info(request.POST)

        elif 'Delete' in request.POST:
            message = db.delete_patient(request.POST)
            print(message)

    context = {'message':message}
    return render(request, 'hms/receptionist/receptionist_patient.html', context)

def Get_Visit_Info(request):
    if request.POST:
        querySet, message = db.get_visit_info(request.POST)
    context = {'querySet':querySet, 'message':message}
    return render(request, 'hms/receptionist/receptionist_visit.html', context)

def Create_Visit(request):
    if request.POST:
        result = db.create_visit(request.POST)
        message = result
    else:
        message = None
    context = {'message':message}
    return render(request, 'hms/receptionist/receptionist_visit.html', context)

def Update_Visit(request):
    if request.POST:
        if 'Update' in request.POST:
            message = db.update_visit_info(request.POST)

        elif 'Delete' in request.POST:
            message = db.delete_visit(request.POST)

    context = {'message':message}
    return render(request, 'hms/receptionist/receptionist_visit.html', context)

def Get_Admission_Info(request):
    if request.POST:
        querySet, message = db.get_admission_info(request.POST)
    context = {'querySet':querySet, 'message':message}
    return render(request, 'hms/receptionist/receptionist_admission.html', context)

def Create_Admission(request):
    if request.POST:
        result = db.create_admission(request.POST)
        message = result
    else:
        message = None
    context = {'message':message}
    return render(request, 'hms/receptionist/receptionist_admission.html', context)

#-------------------------------------------------------
#Admin Staff Page
#-------------------------------------------------------

def Register_Doctor(request):
    if request.POST:
        result = db.register_new_doctor(request.POST)
        message = result

    if request.GET:
        message = None

    context = {'message':message}
    return render(request, 'hms/admin_staff.html', context)


def Update_Admission(request):
    if request.POST:
        if 'Update' in request.POST:
            message = db.update_admission_info(request.POST)

        elif 'Delete' in request.POST:
            print('delete view admission works')
            message = db.delete_admission(request.POST)
    context = {'message':message}
    return render(request, 'hms/receptionist/receptionist_admission.html', context)

def Get_Appointment_Info(request):
    if request.POST:
        querySet, message = db.get_appointment_info(request.POST)
    context = {'querySet':querySet, 'message':message}
    return render(request, 'hms/receptionist/receptionist_appointment.html', context)

def Create_Appointment(request):
    if request.POST:
        result = db.create_appointment(request.POST)
        message = result
    else:
        message = None
    context = {'message':message}
    return render(request, 'hms/receptionist/receptionist_appointment.html', context)

def Update_Appointment(request):
    if request.POST:
        if 'Update' in request.POST:
            message = db.update_appointment_info(request.POST)

        elif 'Delete' in request.POST:
            message = db.delete_appointment(request.POST)

    context = {'message':message}
    return render(request, 'hms/receptionist/receptionist_appointment.html', context)


def Create_Consultation(request):
    print("view_works")
    if request.POST:
        result = db.create_consultation(request.POST)
        message = result
    else:
        message = None
    context = {'message':message}
    return render(request, 'hms/receptionist/receptionist_consultation.html', context)

def Update_Consultation_Info(request):
    print("view works")
    if request.POST:
        if 'Update' in request.POST:
            message = db.update_consultation_info(request.POST)

        elif 'Delete' in request.POST:
            message = db.delete_consultation(request.POST)

    context = {'message':message}
    return render(request, 'hms/receptionist/receptionist_consultation.html', context)


#-------------------------------------------------------
#Admin Logistics Page
#-------------------------------------------------------


def Create_Room(request):
    if request.POST:
        result = db.create_room(request.POST)
        message = result

    if request.GET:
        message = None

    context = {'message':message}
    return render(request, 'hms/admin_logistics.html', context)


def Get_Room_Info(request):
    if request.POST:
        querySet, message = db.get_room_info(request.POST)

    context = {'querySet':querySet, 'message':message}
    return render(request, 'hms/admin_logistics.html', context)


def Update_Room_Info(request):
    if request.POST:
        if 'Update' in request.POST:
            message = db.update_room_info(request.POST)

        elif 'Delete' in request.POST:
            message = db.delete_room(request.POST)

    context = {'message':message}
    return render(request, 'hms/admin_logistics.html', context)


#-------------------------------------------------------
#Admin Medical Page
#-------------------------------------------------------


def Insert_Operation(request):
    if request.POST:
        result = db.insert_operation(request.POST)
        message = result

    if request.GET:
        message = None

    context = {'message':message}
    return render(request, 'hms/admin_medicine.html', context)


def Insert_Medicine(request):
    if request.POST:
        result = db.insert_medicine(request.POST)
        message = result

    if request.GET:
        message = None

    context = {'message':message}
    return render(request, 'hms/admin_medicine.html', context)


def Insert_Test(request):
    if request.POST:
        result = db.insert_test(request.POST)
        message = result

    if request.GET:
        message = None

    context = {'message':message}
    return render(request, 'hms/admin_medicine.html', context)

def Get_Medical_Info(request):
    type = request.POST.get('medical')
    if request.POST:
        if type == "medicine":
            querySet, message = db.get_medicine_info(request.POST)
        if type == "operation":
            querySet, message = db.get_operation_info(request.POST)
        if type == "test":
            querySet, message = db.get_test_info(request.POST)

    context = {'querySet':querySet, 'message':message}
    return render(request, 'hms/admin_medicine.html', context)

def Update_Medical_Info(request):
    if request.POST:
        if 'Update' in request.POST:
            message = db.update_medical_info(request.POST)

        elif 'Delete' in request.POST:
            message = db.delete_room(request.POST)

    context = {'message':message}
    return render(request, 'hms/admin_logistics.html', context)

def Get_Consultation_Info(request):
    if request.POST:
        querySet, message = db.get_consultation_info(request.POST)
    context = {'querySet':querySet, 'message':message}
    return render(request, 'hms/receptionist/receptionist_consultation.html', context)

def Visit(request):
    return render(request, 'hms/receptionist/receptionist_visit.html')

def Patient(request):
    return render(request, 'hms/receptionist/receptionist_patient.html')

def Admission(request):
    return render(request, 'hms/receptionist/receptionist_admission.html')

def Appointment(request):
    return render(request, 'hms/receptionist/receptionist_appointment.html')

def Consultation(request):
    return render(request, 'hms/receptionist/receptionist_consultation.html')
