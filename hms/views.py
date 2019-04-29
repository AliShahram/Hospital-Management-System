from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .Execute_SQL_Queries import *

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
    status = db.validate_employee(e_id)
    if status is True:
        employee_type = db.ident_employee_type(e_id)
        if employee_type:
            if employee_type == 'd':
                return render(request, 'hms/doctor.html')
            elif employee_type == 'r':
                return render(request, 'hms/receptionist.html')
            elif employee_type == 'a':
                return render(request, 'hms/admin_staff.html')
    else:
        message = 'Employee not registered or inactive'
        context = {'message':message}
        return render(request, 'hms/login.html', context )


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


def Register_Recep(request):
    if request.POST:
        result = db.register_new_recep(request.POST)
        message = result

    if request.GET:
        message = None

    context = {'message':message}
    return render(request, 'hms/admin_staff.html', context)


def Get_Employee_Info(request):
    if request.POST:
        querySet, message = db.get_employee_info(request.POST)

    context = {'querySet':querySet, 'message':message}
    return render(request, 'hms/admin_staff.html', context)


def Update_Employee_Info(request):
    if request.POST:
        if 'Update' in request.POST:
            message = db.update_employee_info(request.POST)

        elif 'Delete' in request.POST:
            message = db.delete_employee(request.POST)

    context = {'message':message}
    return render(request, 'hms/admin_staff.html', context)

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
