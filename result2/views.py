from django.shortcuts import render, get_object_or_404, redirect
from .models import Njala_Faculty, Njala_Department, Njala_Program,Njala_Student
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from openpyxl import load_workbook
import pandas as pd
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError


# ============================ADMIN INTERFACE====================
# **************ADMIN LOGIN***********************.

def admin2(request):
    faculty_count = Njala_Faculty.objects.all().count()
    student_count = Njala_Student.objects.all().count()
    department_count = Njala_Department.objects.all().count()
    program_count = Njala_Program.objects.all().count()
    # result_count = Njala_Result.objects.all().count()
    context = {
        'faculty_count':faculty_count,
        'student_count':student_count,
        'department_count':department_count,
        'program_count':program_count,
        # 'result_count':result_count,
    }
    return render(request, 'result/admin2.html', context)

# **************EXAMS OFFICER LOGIN***********************.


# **************ADMIN LOGIN***********************.
def admin_redirect(request):
    return redirect('admin:index')

def login_register(request):
    return render(request, 'result/login_register.html',{})