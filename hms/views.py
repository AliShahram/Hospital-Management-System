from django.shortcuts import render
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
            return render(request, 'hms/doctor.html')
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


def Register_Doctor(request):
    if request.POST:
        result = db.register_new_doctor(request.POST)
        message = result

    if request.GET:
        message = None

    context = {'message':message}
    return render(request, 'hms/admin.html', context)
