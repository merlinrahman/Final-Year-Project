from django.shortcuts import render, get_object_or_404, redirect
from .models import Faculty, Department, Program,Courses,Student,Result
from django.contrib.auth.decorators import login_required
from .forms import FacultyForm, DepartmentForm,UploadFileForm, ProgramForm,CourseForm,FacultyFileForm,CourseFileForm,ProgramFileForm,StudentForm,ResultForm
from django.contrib import messages
from openpyxl import load_workbook
import pandas as pd
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.db.models import Count






# **************INDEX PAGE***********************.
def index(request):
    return render(request, 'result/index.html',{})

# **************ABOUT PAGE***********************.
def about(request):
    return render(request, 'result/about.html',{})

# **************CONTACT PAGE***********************.
def contact(request):
    return render(request, 'result/contact.html',{})

# **************CONTACT PAGE***********************.
def login_register(request):
    return render(request, 'result/login_register.html',{})


# **************CUSL HOME PAGE***********************.
def cusl_home(request):
    return render(request, 'result/cusl_home.html',{})

# **************CUSL HOME PAGE***********************.
def njala_home(request):
    return render(request, 'result/njala_home.html',{})

# **************ADMIN LOGIN***********************.
@login_required(login_url='login')
def admin1(request):
    faculty_count = Faculty.objects.all().count()
    student_count = Student.objects.all().count()
    department_count = Department.objects.all().count()
    program_count = Program.objects.all().count()
    result_count = Result.objects.all().count()
    context = {
        'faculty_count':faculty_count,
        'student_count':student_count,
        'department_count':department_count,
        'program_count':program_count,
        'result_count':result_count,
    }
    return render(request, 'result/admin1.html', context)





# **************EXAMS OFFICER LOGIN***********************.
@login_required(login_url='login')
def admin_login(request):
    return render(request, 'result/admin_login.html',{})

# **************ADMIN LOGIN***********************.
def admin_redirect(request):
    return redirect('admin:index')




# # ***************************************
#                  # UNIVERSITIES
# #*****************************************
# # *********ADD UNIVERSITY***********
# def university(request):
#     university = University.objects.all()
#     if request.method == 'POST':
#         form =UniversityForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "University added Successfully")
#             return redirect('university')
#     else:
#         form = UniversityForm()
#     return render(request, 'result/university.html',{'university':university,'form':form})



# # *********DELETE UNIVERSITY***********
# def delete_university(request, pk):
#     university = University.objects.get(id=pk)
#     if request.method == 'POST':
#         university.delete()
#         messages.success(request, "University has been removed!")
#         return redirect('university')
#     return render(request, 'result/delete_university.html',{})

# # *********EDIT UNIVERSITY***********

# def edit_university(request, pk):
#     edituni = University.objects.get(id=pk)
#     if request.method == 'POST':
#         form = UniversityForm(request.POST, instance = edituni)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "University has been updated successfully!")
#             return redirect('university')
#     else:
#         form = UniversityForm(instance = edituni)

#     return render(request, 'result/edit_university.html',{'form':form})


# # ****************VIEW UNIVERSITY******************

# def view_university(request, pk):
#     univer = University.objects.get(id=pk)
#     return render(request, 'result/view_university.html', {'univer': univer})



# # ****************UPLOAD UNIVERSITY******************
# def upload_university(request):
#     if request.method == 'POST':
#         form = UniversityFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             file = request.FILES['file']
#             data = pd.read_excel(file)
#             for index, row in data.iterrows():
#                 university = row.get('university', '')  # set name to empty string if not present in row
#                 uni_number = row.get('uni_number', '')  # set code to empty string if not present in row
#                 university = University(university=university,uni_number=uni_number)
#                 university.save()
#             messages.success(request, "University uploaded successfully!")
#             return redirect('university')
#         else:
#             messages.error(request, "Invalid form submission!")
#     else:
#         form = UniversityFileForm()
#     return render(request, 'result/uploadUniversity.html', {'form': form})










# ***************************************
                 # FACULTIES
#*****************************************
# *********ADD FACULTY***********
def faculty(request):
    facult = Faculty.objects.all()
    if request.method == 'POST':
        form =FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Faculty has been updated !")
            return redirect('faculty')
    else:
        form = FacultyForm()
    return render(request, 'result/faculty.html',{'facult':facult,'form':form})


# *********DELETE FACULTY***********
def delete_faculty(request, pk):
    facult = Faculty.objects.get(id=pk)
    if request.method == 'POST':
        facult.delete()
        messages.success(request, "Faculty has been removed!")
        return redirect('faculty')
    return render(request, 'result/delete_faculty.html',{})

# *********EDIT FACULTY***********

def edit_faculty(request, pk):
    editfac = Faculty.objects.get(id=pk)
    if request.method == 'POST':
        form = FacultyForm(request.POST, instance = editfac)
        if form.is_valid():
            form.save()
            messages.success(request, "Faculty has been updated successfully!")
            return redirect('faculty')
    else:
        form = FacultyForm(instance = editfac)

    return render(request, 'result/edit_faculty.html',{'form':form})


# ****************VIEW FACULTY******************

def view_faculty(request, pk):
    facult = Faculty.objects.get(id=pk)
    return render(request, 'result/view_Faculty.html', {'facult': facult})



# ****************FACULTY UPLOAD FILE******************
def upload_faculty(request):
    if request.method == 'POST':
        form = FacultyFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            for index, row in data.iterrows():
                faculty_name = row.get('faculty', '')  # Set name to empty string if not present in row
                faculty = Faculty(faculty=faculty_name)
                faculty.save()
            messages.success(request, "Faculty uploaded successfully!")
            return redirect('faculty')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = FacultyFileForm()
    return render(request, 'result/uploadFaculty.html', {'form': form})









# ***************************************
                 # DEPARTMENTS
#*****************************************
# *********ADD DEPARTMENT***********

def department(request):
    all_dept = Department.objects.all()
    if request.method == 'POST':
        form =DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Department has been updated !")
            return redirect('department')
    else:
        form = DepartmentForm()
    return render(request, 'result/department.html',{'all_dept':all_dept,'form':form})

# *********DELETE FACULTY***********
def delete_department(request, pk):
    dept = Department.objects.get(id=pk)
    if request.method == 'POST':
        dept.delete()
        messages.success(request, "Department removed successfully! ")
        return redirect('department')
    return render(request, 'result/delete_department.html',{})

# *********EDIT DEPARTMENT***********
def edit_department(request, pk):
    editfac = Department.objects.get(id=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance = editfac)
        if form.is_valid():
            form.save()
            messages.success(request, "Department updated successfully!")
            return redirect('department')
    else:
        form = DepartmentForm(instance = editfac)

    return render(request, 'result/edit_department.html',{'form':form})


# ****************VIEW DEPARTMENT******************

def view_department(request, pk):
    dept = Department.objects.get(id=pk)
    return render(request, 'result/view_department.html', {'dept': dept})


# ****************DEPARTMENT UPLOAD FILE******************
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # read the excel file
            excel_file = request.FILES['file']
            df = pd.read_excel(excel_file)
            # create a new instance of Department for each row of data and save it to the database
            for index, row in df.iterrows():
                faculty_name = row['faculty']
                try:
                    faculty = Faculty.objects.get(faculty=faculty_name)
                except Faculty.DoesNotExist:
                    # handle the case where the Faculty doesn't exist
                    messages.error(request, f"Faculty {faculty_name} does not exist.")
                    return redirect('department')
                except Faculty.MultipleObjectsReturned:
                    # handle the case where multiple Faculties with the same name exist
                    messages.warning(request, f"Multiple Faculties with the name {faculty_name} exist. Using the first one found.")
                    faculty = Faculty.objects.filter(name=faculty_name).first()
                department = Department(faculty=faculty, department=row['department'])
                department.save()
            # redirect to a success page
            messages.success(request, "Departments have been added successfully!")
            return redirect('department')
    else:
        form = UploadFileForm()
    return render(request, 'result/uploadDepartment.html', {'form': form})















# ***************************************
                 # PROGRAMS
#*****************************************

# *********ADD PROGRAMS***********
def programs(request):
    all_prog = Program.objects.all()
    if request.method == 'POST':
        form =ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Program has been updated !")
            return redirect('programs')
    else:
        form = ProgramForm()
    return render(request, 'result/programs.html',{'all_prog':all_prog,'form':form})



# *********EDIT PROGRAM***********
def edit_program(request, pk):
    editprog = Program.objects.get(id=pk)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance = editprog)
        if form.is_valid():
            form.save()
            messages.success(request, "program updated successfully!")
            return redirect('programs')
    else:
        form = ProgramForm(instance = editprog)

    return render(request, 'result/edit_programs.html',{'form':form})


# *********DELETE PROGRAM***********
def delete_program(request, pk):
    prog = Program.objects.get(id=pk)
    if request.method == 'POST':
        prog.delete()
        messages.success(request, "program removed successfully! ")
        return redirect('programs')
    return render(request, 'result/delete_programs.html',{})



# ****************VIEW DEPARTMENT******************

def view_program(request, pk):
    prog = Program.objects.get(id=pk)
    return render(request, 'result/view_programs.html', {'prog': prog})



# ****************PROGRAM UPLOAD FILE******************
# def upload_programs(request):
#     if request.method == 'POST':
#         form = ProgramFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # read the excel file
#             excel_file = request.FILES['file']
#             df = pd.read_excel(excel_file)
#             # create a new instance of Department for each row of data and save it to the database
#             for index, row in df.iterrows():
#                 department_name = row['department']
#                 try:
#                     department = Department.objects.get(name=department_name)
#                 except Department.DoesNotExist:
#                     # handle the case where the Faculty doesn't exist
#                     messages.error(request, f"Department {department_name} does not exist.")
#                     return redirect('programs')
#                 except Department.MultipleObjectsReturned:
#                     # handle the case where multiple Faculties with the same name exist
#                     messages.warning(request, f"Multiple Department with the name {department_name} exist. Using the first one found.")
#                     department= Department.objects.filter(name=department_name).first()
#                 program = Program(department=department, name=row['name'])
#                 program.save()
#             # redirect to a success page
#             messages.success(request, "Position have been added successfully!")
#             return redirect('program')
#     else:
#         form = ProgramFileForm()
#     return render(request, 'result/uploadDepartment.html', {'form': form})


def upload_programs(request):
    if request.method == 'POST':
        form = ProgramFileForm(request.POST, request.FILES)
        if form.is_valid():
            # read the excel file
            excel_file = request.FILES['file']
            df = pd.read_excel(excel_file)

            # create a new instance of Program for each row of data and save it to the database
            for index, row in df.iterrows():
                department_name = row['department']
                try:
                    department = Department.objects.get(name=department_name)
                except Department.DoesNotExist:
                    # handle the case where the Department doesn't exist
                    messages.error(request, f"Department {department_name} does not exist.")
                    return redirect('programs')
                except Department.MultipleObjectsReturned:
                    # handle the case where multiple Departments with the same name exist
                    messages.warning(request, f"Multiple Departments with the name {department_name} exist. Using the first one found.")
                    department = Department.objects.filter(name=department_name).first()

                program_name = row['name']
                if Program.objects.filter(name=program_name).exists():
                    # handle the case where a program with the same name already exists
                    messages.warning(request, f"Program with the name {program_name} already exists. Skipping this program.")
                    continue

                program = Program(department=department, name=program_name)
                program.save()

            # redirect to a success page
            messages.success(request, "Programs have been added successfully!")
            return redirect('programs')
        else:
            messages.error(request, "Invalid form submission. Please check the form fields.")
            return redirect('programs')
    else:
        form = ProgramFileForm()
    return render(request, 'result/uploadPrograms.html', {'form': form})



















# ***************************************
                 # COURSE/MODULE
#*****************************************

# *********ADD SEMESTER***********
def course(request):
    cos = Courses.objects.all()
    if request.method == 'POST':
        form =CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added Successfully!")
            return redirect('course')
    else:
        form = CourseForm()
    return render(request, 'result/course.html',{'cos':cos,'form':form})



# *********EDIT COURSE***********
def edit_course(request, pk):
    editcos = Courses.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance = editcos)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('course')
    else:
        form = CourseForm(instance = editcos)

    return render(request, 'result/edit_course.html',{'form':form})


# *********DELETE SEMESTER***********
def delete_course(request, pk):
    del_cos = Courses.objects.get(id=pk)
    if request.method == 'POST':
        del_cos.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('course')
    return render(request, 'result/delete_course.html',{})


# ****************VIEW COURSE******************
def view_course(request, pk):
    cos = Courses.objects.get(id=pk)
    return render(request, 'result/view_course.html', {'cos': cos})


# ****************UPLOAD COURSE******************
def upload_course(request):
    if request.method == 'POST':
        form = CourseFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            for index, row in data.iterrows():
                code = row.get('code', '')  # set code to empty string if not present in row
                course = row.get('course', '')  # set name to empty string if not present in row
                course = Courses(code=code, course=course)
                course.save()
            messages.success(request, "Course uploaded successfully!")
            return redirect('course')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = CourseFileForm()
    return render(request, 'result/uploadCourses.html', {'form': form})









# ***************************************
                 # STUDENTS
#*****************************************

# ****************STUDENT REGISTRATION******************
def register_student(request):
    return render(request, 'result/register_student.html', {})



# ****************STUDENT******************
# *********ADD STUDENTS***********
def student(request):
    stu = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
                form.save()
                messages.success(request, "Student added successfully!")
                return redirect('student')
    else:
        form = StudentForm()
    return render(request, 'result/student.html', {'stu': stu, 'form': form})




# **************EDIT STUDENT***********
def edit_student(request, pk):
    editstu = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance = editstu)
        if form.is_valid():
            form.save()
            messages.success(request, "Students updated successfully!")
            return redirect('student')
    else:
        form = StudentForm(instance = editstu)

    return render(request, 'result/edit_student.html',{'form':form})


# *********DELETE STUDENT***********
def delete_student(request, pk):
    del_stu = Student.objects.get(id=pk)
    if request.method == 'POST':
        del_stu.delete()
        messages.success(request, "Student removed successfully! ")
        return redirect('student')
    return render(request, 'result/delete_student.html',{})


# ****************VIEW LEVEL******************
def view_student(request, pk):
    viewstu = Student.objects.get(id=pk)
    return render(request, 'result/view_student.html', {'viewstu': viewstu})




# ***********************************************************************AUTHENTICATION*********************************************************

#********************REGISTER********************
def register(request):
    if request.method == 'POST':
        fullName = request.POST['fullName']
        email = request.POST['email']
        password =request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already exist ')
                return redirect(register)
            else:
                user = User.objects.create_user(fullName=fullName,email=email,password=password)
                user.set_password(password)
                user.save()
                messages.success(request, "Student registered successfully! ")
                return redirect('register')
    else:
        return render(request, 'result/register.html', {})
    



def student_login(request):
    if request.method == 'POST':
        email =request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('cusl_home')
        else:
            messages.info(request, 'Invalid Email or Password')
            return redirect('login')
    else:
        return render(request, 'result/cusl_home.html',{})
    
@login_required(login_url='login')
def student_home(request):
    return render(request, 'result/cusl_home.html')


def student_logout(request):
    auth.logout(request)
    return redirect('login_registered')














































# # ***************************************
#                  # STUDENTS RESULT
# #*****************************************

def result(request):
    results_entry = Result.objects.all()
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.save()
            messages.success(request, "Results added successfully!")
            return redirect('result')
        else:
            messages.error(request, "There was an error adding the results.")
    else:
        form = ResultForm()
    return render(request, 'result/result.html', {'results_entry':results_entry,'form': form})




# **************EDIT Result***********
def edit_result(request, pk):
    editres = Result.objects.get(id=pk)
    if request.method == 'POST':
        form = ResultForm(request.POST, instance = editres)
        if form.is_valid():
            form.save()
            messages.success(request, "Result updated successfully!")
            return redirect('result')
    else:
        form = ResultForm(instance = editres)

    return render(request, 'result/edit_result.html',{'form':form})



# *********DELETE STUDENT***********
def delete_result(request, pk):
    del_result = Result.objects.get(id=pk)
    if request.method == 'POST':
        del_result.delete()
        messages.success(request, "Result removed successfully! ")
        return redirect('result')
    return render(request, 'result/delete_result.html',{})



# *********VIEW RESULT***********
def view_result(request, pk):
    viewresult = Result.objects.get(id=pk)
    return render(request, 'result/view_result.html', {'viewresult': viewresult})





# ****************************************************

#***********SEARCHING FOR THE RESULT*************

# ****************************************************
def search_result(request):
    email = request.GET.get('email')
    id_number = request.GET.get('id_number')
    result = None

    if email and id_number:
        try:
            result = Result.objects.get(student__email=email, student__student_id=id_number)
        except Result.DoesNotExist:
            result = None

    context = {
        'result': result,
    }
    return render(request, 'result/view_student_result.html', context)



# ****************************************************

#***********DISPLAYING THE RESULT*************

# ****************************************************

def view_student_result(request, email, id_number):
    try:
        result = Result.objects.get(student__email=email, student__student_id=id_number)
    except Result.DoesNotExist:
        result = None

    context = {
        'result': result,
    }
    return render(request, 'result_display.html', context)