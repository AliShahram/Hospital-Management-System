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

    print(employee_type[0])
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
