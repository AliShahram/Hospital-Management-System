from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from .Execute_SQL_Queries import *

# Create your views here.

db = Database()

def emp_login(request):
    return render(request, 'hms/login.html')

def HomePage(request):
    e_id = request.GET.get('e_id')
    employee_type = db.ident_employee_type(e_id)
    if employee_type:
        if employee_type == 'd':
            return redirect('/DoctorHomePage')
        elif employee_type == 'r':
            return render(request, 'hms/receptionist.html')
        elif employee_type == 'a':
            return render(request, 'hms/admin.html')
    else:
        context = {'emp':e_id}
        return render(request, 'hms/login.html', context )



#-------------------------------------------------------
#Admin HomePage
#-------------------------------------------------------

def DoctorHomePage(request):

    medicine = db.get_medicine_name()
    operation = db.get_operation_name()
    testing = db.get_test_name()
    context = {
    'medicine': medicine,
    "operation": operation,
    "testing": testing
    }


    return render(request, 'hms/doctor.html', context)

def get_all_medicine(request):
    if request.POST:
        result = db.get_medicine_name(request.POST)
        message = result

    if request.GET:
        message = None

    context = {'message':message}
    return render(request, 'hms/doctor.html', context)

def Register_Doctor(request):
    if request.POST:
        result = db.register_new_doctor(request.POST)
        message = result

    if request.GET:
        message = None

    context = {'message':message}
    return render(request, 'hms/admin.html', context)


def register_operation(request):

    if request.POST:

        result = db.register_opeartion(request.POST)
        message = result

    if request.GET:
        message = None

    context = {'message':message}
    #return render(request, 'hms/doctor.html', context)
    return redirect('/DoctorHomePage', context)

def register_prescription(request):

    if request.POST:
        result = db.register_prescription(request.POST)
        message = result

    if request.GET:
        message = None

    context = {'message':message}
    #return render(request, 'hms/doctor.html', context)
    return redirect('/DoctorHomePage', context)

def register_testing(request):

    if request.POST:
        result = db.register_testing(request.POST)
        message = result

    if request.GET:
        message = None

    context = {'message':message}
    #return render(request, 'hms/doctor.html', context)
    return redirect('/DoctorHomePage', context)

def get_medical_history(request):

    if request.POST:
        p_operation, p_prescription, p_test, message = db.get_medical_history(request.POST)
    print(p_operation, p_prescription, p_test, message)
    context_history = {'p_operation':p_operation, 'p_prescription': p_prescription, 'p_test': p_test, 'message':message}
    return redirect('/DoctorHomePage', context_history)
