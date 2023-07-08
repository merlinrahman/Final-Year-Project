from django.shortcuts import render, get_object_or_404, redirect
from .models import Faculty, Department, Program,Student,Result,year1_semester1,year1_semester2,year2_semester1,year2_semester2,year3_semester1,year3_semester2,year4_semester1,year4_semester2
from django.contrib.auth.decorators import login_required
from .forms import FacultyForm, DepartmentForm,UploadFileForm,StudentFileForm,ProgramForm,FacultyFileForm,CourseFileForm,ProgramFileForm,StudentForm,ResultForm,CourseForm1,CourseForm2,CourseForm3,CourseForm4,CourseForm5,CourseForm6,CourseForm7,CourseForm8
from django.contrib import messages
from openpyxl import load_workbook
import pandas as pd
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError





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
            # Read the excel file
            excel_file = request.FILES['file']
            df = pd.read_excel(excel_file)
            
            # Iterate over each row and save departments to the database
            for index, row in df.iterrows():
                faculty_name = row['faculty']
                try:
                    faculty = Faculty.objects.get(faculty=faculty_name)
                except Faculty.DoesNotExist:
                    # Handle the case where the Faculty doesn't exist
                    messages.error(request, f"Faculty {faculty_name} does not exist.")
                    return redirect('department')
                except Faculty.MultipleObjectsReturned:
                    # Handle the case where multiple Faculties with the same name exist
                    messages.warning(request, f"Multiple Faculties with the name {faculty_name} exist. Using the first one found.")
                    faculty = Faculty.objects.filter(faculty=faculty_name).first()
                    
                department_name = row['department']
                department = Department(faculty=faculty, department=department_name)
                department.save()
            
            # Redirect to a success page
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
def upload_programs(request):
    if request.method == 'POST':
        form = ProgramFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            try:
                df = pd.read_excel(excel_file)
            except Exception as e:
                messages.error(request, "An error occurred while reading the Excel file.")
                return redirect('programs')

            programs_added = 0
            programs_skipped = 0

            for _, row in df.iterrows():
                program_name = row['program']
                department_name = row['department']

                try:
                    faculty = Faculty.objects.first()  # Replace with the appropriate logic to get the faculty
                    department, _ = Department.objects.get_or_create(department=department_name, faculty=faculty)
                except Department.DoesNotExist:
                    messages.error(request, f"Department '{department_name}' does not exist.")
                    return redirect('programs')
                except Department.MultipleObjectsReturned:
                    messages.warning(request, f"Multiple Departments with the name '{department_name}' exist. Using the first one found.")
                    department = Department.objects.filter(department=department_name, faculty=faculty).first()

                if Program.objects.filter(program=program_name, department=department).exists():
                    messages.warning(request, f"Program '{program_name}' in Department '{department_name}' already exists. Skipping this program.")
                    programs_skipped += 1
                    continue

                program = Program(program=program_name, department=department)
                program.save()
                programs_added += 1

            if programs_added > 0:
                messages.success(request, f"{programs_added} program(s) have been added successfully!")
            if programs_skipped > 0:
                messages.warning(request, f"{programs_skipped} program(s) already exist and were skipped.")

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

# *********ADD year1_first_semester***********
def year1_first_semester(request):
    yr1_sem1 = year1_semester1.objects.all()
    if request.method == 'POST':
        form =CourseForm1(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added Successfully!")
            return redirect('year1_first_semester')
    else:
        form = CourseForm1()
    return render(request, 'result/year1_first_semester.html',{'yr1_sem1':yr1_sem1,'form':form})



# *********EDIT year1_first_semester***********
def edit_year1_first_semester(request, pk):
    edit_yr1_sem1 = year1_semester1.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm1(request.POST, instance = edit_yr1_sem1)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('year1_first_semester')
    else:
        form = CourseForm1(instance = edit_yr1_sem1)

    return render(request, 'result/edit_year1_first_semester.html',{'form':form})


# *************DELETE year1_first_semester*****************
def delete_year1_first_semester(request, pk):
    del_yr1_sem1 = year1_semester1.objects.get(id=pk)
    if request.method == 'POST':
        del_yr1_sem1.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('year1_first_semester')
    return render(request, 'result/delete_year1_first_semester.html',{})



# ****************VIEW year1_first_semester******************
def view_year1_first_semester(request, pk):
    view_yr1_sem1 = year1_semester1.objects.get(id=pk)
    return render(request, 'result/view_year1_first_semester.html', {'view_yr1_sem1': view_yr1_sem1})

# ****************year1_semester1 UPLOAD FILE******************
def upload_course(request):
    if request.method == 'POST':
        form = CourseFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create the new course instance
                    program, created = Program.objects.get_or_create(program=program_name)
                    course_instance = year1_semester1.objects.create(
                        code=code,
                        course=course,
                        program=program,
                        level=level,
                        semester=semester
                    )
                except IntegrityError:
                    # Handle duplicate code values here
                    existing_course = year1_semester1.objects.get(code=code)
                    # Update the existing course with the new values
                    existing_course.course = course
                    existing_course.program = program
                    existing_course.level = level
                    existing_course.semester = semester
                    existing_course.save()

            messages.success(request, "Courses uploaded successfully!")
            return redirect('year1_first_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = CourseFileForm()
    return render(request, 'result/upload_year1_first_semester.html', {'form': form})





# *********ADD year1_second_semester***********
def year1_second_semester(request):
    yr1_sem2 = year1_semester2.objects.all()
    if request.method == 'POST':
        form =CourseForm2(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added Successfully!")
            return redirect('year1_second_semester')
    else:
        form = CourseForm2()
    return render(request, 'result/year1_second_semester.html',{'yr1_sem2':yr1_sem2,'form':form})



# *********EDIT year1_second_semester***********
def edit_year1_second_semester(request, pk):
    edit_yr1_sem2 = year1_semester2.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm2(request.POST, instance = edit_yr1_sem2)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('year1_second_semester')
    else:
        form = CourseForm2(instance = edit_yr1_sem2)

    return render(request, 'result/edit_year1_second_semester.html',{'form':form})


# *************DELETE year1_second_semester*****************
def delete_year1_second_semester(request, pk):
    del_yr1_sem2 = year1_semester2.objects.get(id=pk)
    if request.method == 'POST':
        del_yr1_sem2.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('year1_second_semester')
    return render(request, 'result/delete_year1_second_semester.html',{})



# ****************VIEW year1_first_semester******************
def view_year1_second_semester(request, pk):
    view_yr1_sem2 = year1_semester2.objects.get(id=pk)
    return render(request, 'result/view_year1_first_semester.html', {'view_yr1_sem2': view_yr1_sem2})

# ****************year1_semester1 UPLOAD FILE******************
def upload_course2(request):
    if request.method == 'POST':
        form = CourseFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create the new course instance
                    program, created = Program.objects.get_or_create(program=program_name)
                    course_instance = year1_semester2.objects.create(
                        code=code,
                        course=course,
                        program=program,
                        level=level,
                        semester=semester
                    )
                except IntegrityError:
                    # Handle duplicate code values here
                    existing_course = year1_semester2.objects.get(code=code)
                    # Update the existing course with the new values
                    existing_course.course = course
                    existing_course.program = program
                    existing_course.level = level
                    existing_course.semester = semester
                    existing_course.save()

            messages.success(request, "Courses uploaded successfully!")
            return redirect('year1_second_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = CourseFileForm()
    return render(request, 'result/upload_year1_second_semester.html', {'form': form})








# *********ADD year2_first_semester***********
def year2_first_semester(request):
    yr2_sem1 = year2_semester1.objects.all()
    if request.method == 'POST':
        form =CourseForm3(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added Successfully!")
            return redirect('year2_first_semester')
    else:
        form = CourseForm3()
    return render(request, 'result/year2_first_semester.html',{'yr2_sem1':yr2_sem1,'form':form})



# *********EDIT year2_first_semester***********
def edit_year2_first_semester(request, pk):
    edit_yr2_sem1 = year2_semester1.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm3(request.POST, instance = edit_yr2_sem1)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('year2_first_semester')
    else:
        form = CourseForm3(instance = edit_yr2_sem1)

    return render(request, 'result/edit_year2_first_semester.html',{'form':form})


# *************DELETE year2_first_semester*****************
def delete_year2_first_semester(request, pk):
    del_yr2_sem1 = year2_semester1.objects.get(id=pk)
    if request.method == 'POST':
        del_yr2_sem1.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('year2_first_semester')
    return render(request, 'result/delete_year2_first_semester.html',{})



# ****************VIEW year2_first_semester******************
def view_year2_first_semester(request, pk):
    view_yr2_sem1 = year2_semester1.objects.get(id=pk)
    return render(request, 'result/view_year2_first_semester.html', {'view_yr2_sem2': view_yr2_sem1})

# ****************year1_semester1 UPLOAD FILE******************
def upload_course3(request):
    if request.method == 'POST':
        form = CourseFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create the new course instance
                    program, created = Program.objects.get_or_create(program=program_name)
                    course_instance = year2_semester1.objects.create(
                        code=code,
                        course=course,
                        program=program,
                        level=level,
                        semester=semester
                    )
                except IntegrityError:
                    # Handle duplicate code values here
                    existing_course = year2_semester1.objects.get(code=code)
                    # Update the existing course with the new values
                    existing_course.course = course
                    existing_course.program = program
                    existing_course.level = level
                    existing_course.semester = semester
                    existing_course.save()

            messages.success(request, "Courses uploaded successfully!")
            return redirect('year2_first_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = CourseFileForm()
    return render(request, 'result/upload_year2_first_semester.html', {'form': form})








# *********ADD year2_second_semester***********
def year2_second_semester(request):
    yr2_sem2 = year2_semester2.objects.all()
    if request.method == 'POST':
        form =CourseForm4(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added Successfully!")
            return redirect('year2_second_semester')
    else:
        form = CourseForm4()
    return render(request, 'result/year2_second_semester.html',{'yr2_sem2':yr2_sem2,'form':form})



# *********EDIT year2_second_semester***********
def edit_year2_second_semester(request, pk):
    edit_yr2_sem2 = year2_semester2.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm4(request.POST, instance = edit_yr2_sem2)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('year2_second_semester')
    else:
        form = CourseForm4(instance = edit_yr2_sem2)

    return render(request, 'result/edit_year2_second_semester.html',{'form':form})


# *************DELETE year2_second_semester*****************
def delete_year2_second_semester(request, pk):
    del_yr2_sem2 = year2_semester2.objects.get(id=pk)
    if request.method == 'POST':
        del_yr2_sem2.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('year2_second_semester')
    return render(request, 'result/delete_year2_second_semester.html',{})


# ****************VIEW year2_second_semester******************
def view_year2_second_semester(request, pk):
    view_yr2_sem2 = year2_semester2.objects.get(id=pk)
    return render(request, 'result/view_year2_second_semester.html', {'view_yr2_sem2': view_yr2_sem2})

# ****************year1_semester1 UPLOAD FILE******************
def upload_course4(request):
    if request.method == 'POST':
        form = CourseFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create the new course instance
                    program, created = Program.objects.get_or_create(program=program_name)
                    course_instance = year2_semester2.objects.create(
                        code=code,
                        course=course,
                        program=program,
                        level=level,
                        semester=semester
                    )
                except IntegrityError:
                    # Handle duplicate code values here
                    existing_course = year2_semester2.objects.get(code=code)
                    # Update the existing course with the new values
                    existing_course.course = course
                    existing_course.program = program
                    existing_course.level = level
                    existing_course.semester = semester
                    existing_course.save()

            messages.success(request, "Courses uploaded successfully!")
            return redirect('year2_second_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = CourseFileForm()
    return render(request, 'result/upload_year2_second_semester.html', {'form': form})



# *********ADD year3_first_semester***********
def year3_first_semester(request):
    yr3_sem1 = year3_semester1.objects.all()
    if request.method == 'POST':
        form =CourseForm5(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added Successfully!")
            return redirect('year3_first_semester')
    else:
        form = CourseForm5()
    return render(request, 'result/year3_first_semester.html',{'yr3_sem1':yr3_sem1,'form':form})



# *********EDIT year3_first_semester***********
def edit_year3_first_semester(request, pk):
    edit_yr3_sem1 = year3_semester1.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm5(request.POST, instance = edit_yr3_sem1)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('year3_first_semester')
    else:
        form = CourseForm5(instance = edit_yr3_sem1)

    return render(request, 'result/edit_year3_first_semester.html',{'form':form})


# *************DELETE year3_first_semester*****************
def delete_year3_first_semester(request, pk):
    del_yr3_sem1 = year3_semester1.objects.get(id=pk)
    if request.method == 'POST':
        del_yr3_sem1.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('year3_first_semester.html')
    return render(request, 'result/delete_year3_first_semester.html',{})



# ****************VIEW year3_first_semester******************
def view_year3_first_semester(request, pk):
    view_yr3_sem1 = year3_semester1.objects.get(id=pk)
    return render(request, 'result/view_year3_first_semester.html', {'view_yr3_sem2': view_yr3_sem1})
# ****************year1_semester1 UPLOAD FILE******************
def upload_course5(request):
    if request.method == 'POST':
        form = CourseFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create the new course instance
                    program, created = Program.objects.get_or_create(program=program_name)
                    course_instance = year3_semester1.objects.create(
                        code=code,
                        course=course,
                        program=program,
                        level=level,
                        semester=semester
                    )
                except IntegrityError:
                    # Handle duplicate code values here
                    existing_course = year3_semester1.objects.get(code=code)
                    # Update the existing course with the new values
                    existing_course.course = course
                    existing_course.program = program
                    existing_course.level = level
                    existing_course.semester = semester
                    existing_course.save()

            messages.success(request, "Courses uploaded successfully!")
            return redirect('year3_first_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = CourseFileForm()
    return render(request, 'result/upload_year3_first_semester.html', {'form': form})






# *********ADD year3_second_semester***********
def year3_second_semester(request):
    yr3_sem2 = year3_semester2.objects.all()
    if request.method == 'POST':
        form =CourseForm6(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added Successfully!")
            return redirect('year3_second_semester')
    else:
        form = CourseForm6()
    return render(request, 'result/year3_second_semester.html',{'yr3_sem2':yr3_sem2,'form':form})



# *********EDIT year3_second_semester***********
def edit_year3_second_semester(request, pk):
    edit_yr3_sem2 = year3_semester2.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm6(request.POST, instance = edit_yr3_sem2)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('year3_second_semester')
    else:
        form = CourseForm6(instance = edit_yr3_sem2)

    return render(request, 'result/edit_year3_second_semester.html',{'form':form})


# *************DELETE year3_second_semester*****************
def delete_year3_second_semester(request, pk):
    del_yr3_sem2 = year3_semester2.objects.get(id=pk)
    if request.method == 'POST':
        del_yr3_sem2.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('year3_second_semester')
    return render(request, 'result/delete_year3_second_semester.html',{})



# ****************VIEW year3_second_semester******************
def view_year3_second_semester(request, pk):
    view_yr3_sem2 = year3_semester2.objects.get(id=pk)
    return render(request, 'result/view_year3_second_semester.html', {'view_yr3_sem2': view_yr3_sem2})

# ****************year1_semester1 UPLOAD FILE******************
def upload_course6(request):
    if request.method == 'POST':
        form = CourseFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create the new course instance
                    program, created = Program.objects.get_or_create(program=program_name)
                    course_instance = year3_semester2.objects.create(
                        code=code,
                        course=course,
                        program=program,
                        level=level,
                        semester=semester
                    )
                except IntegrityError:
                    # Handle duplicate code values here
                    existing_course = year3_semester2.objects.get(code=code)
                    # Update the existing course with the new values
                    existing_course.course = course
                    existing_course.program = program
                    existing_course.level = level
                    existing_course.semester = semester
                    existing_course.save()

            messages.success(request, "Courses uploaded successfully!")
            return redirect('year3_second_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = CourseFileForm()
    return render(request, 'result/upload_year3_second_semester.html', {'form': form})






# *********EDIT year4_first_semester***********
def edit_year4_first_semester(request, pk):
    edit_yr4_sem1 = year4_semester1.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm7(request.POST, instance = edit_yr4_sem1)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('year4_first_semester')
    else:
        form = CourseForm7(instance = edit_yr4_sem1)

    return render(request, 'result/edit_year4_first_semester.html',{'form':form})


# *************DELETE year4_first_semester*****************
def delete_year4_first_semester(request, pk):
    del_yr4_sem1 = year4_semester1.objects.get(id=pk)
    if request.method == 'POST':
        del_yr4_sem1.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('year4_first_semester')
    return render(request, 'result/delete_year4_first_semester.html',{})



# ****************VIEW year4_first_semester******************
def view_year4_first_semester(request, pk):
    view_yr4_sem1 = year4_semester1.objects.get(id=pk)
    return render(request, 'result/view_year4_first_semester.html', {'view_yr4_sem2': view_yr4_sem1})

# ****************year1_semester1 UPLOAD FILE******************
def upload_course7(request):
    if request.method == 'POST':
        form = CourseFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create the new course instance
                    program, created = Program.objects.get_or_create(program=program_name)
                    course_instance = year4_semester1.objects.create(
                        code=code,
                        course=course,
                        program=program,
                        level=level,
                        semester=semester
                    )
                except IntegrityError:
                    # Handle duplicate code values here
                    existing_course = year4_semester1.objects.get(code=code)
                    # Update the existing course with the new values
                    existing_course.course = course
                    existing_course.program = program
                    existing_course.level = level
                    existing_course.semester = semester
                    existing_course.save()

            messages.success(request, "Courses uploaded successfully!")
            return redirect('year4_first_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = CourseFileForm()
    return render(request, 'result/upload_year4_first_semester.html', {'form': form})



# *********ADD year4_first_semester***********
def year4_first_semester(request):
    yr4_sem1 = year4_semester1.objects.all()
    if request.method == 'POST':
        form =CourseForm7(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added Successfully!")
            return redirect('year4_first_semester')
    else:
        form = CourseForm7()
    return render(request, 'result/year4_first_semester.html',{'yr4_sem1':yr4_sem1,'form':form})





# *********ADD year4_second_semester***********
def year4_second_semester(request):
    yr4_sem2 = year4_semester2.objects.all()
    if request.method == 'POST':
        form =CourseForm8(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added Successfully!")
            return redirect('year4_second_semester')
    else:
        form = CourseForm8()
    return render(request, 'result/year4_second_semester.html',{'yr4_sem2':yr4_sem2,'form':form})



# *********EDIT year4_second_semester***********
def edit_year4_second_semester(request, pk):
    edit_yr4_sem2 = year4_semester2.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm8(request.POST, instance = edit_yr4_sem2)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('year4_second_semester')
    else:
        form = CourseForm8(instance = edit_yr4_sem2)

    return render(request, 'result/edit_year4_second_semester.html',{'form':form})


# *************DELETE year4_second_semester*****************
def delete_year4_second_semester(request, pk):
    del_yr4_sem2 = year4_semester2.objects.get(id=pk)
    if request.method == 'POST':
        del_yr4_sem2.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('year4_second_semester')
    return render(request, 'result/delete_year4_second_semester.html',{})



# ****************VIEW year4_second_semester******************
def view_year4_second_semester(request, pk):
    view_yr4_sem2 = year4_semester1.objects.get(id=pk)
    return render(request, 'result/view_year4_second_semester.html', {'view_yr4_sem2': view_yr4_sem2})

# ****************year1_semester1 UPLOAD FILE******************
def upload_course8(request):
    if request.method == 'POST':
        form = CourseFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create the new course instance
                    program, created = Program.objects.get_or_create(program=program_name)
                    course_instance = year4_semester2.objects.create(
                        code=code,
                        course=course,
                        program=program,
                        level=level,
                        semester=semester
                    )
                except IntegrityError:
                    # Handle duplicate code values here
                    existing_course = year4_semester2.objects.get(code=code)
                    # Update the existing course with the new values
                    existing_course.course = course
                    existing_course.program = program
                    existing_course.level = level
                    existing_course.semester = semester
                    existing_course.save()

            messages.success(request, "Courses uploaded successfully!")
            return redirect('year4_second_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = CourseFileForm()
    return render(request, 'result/upload_year4_second_semester.html', {'form': form})



# *********ADD year4_first_semester***********
def year4_first_semester(request):
    yr4_sem1 = year4_semester1.objects.all()
    if request.method == 'POST':
        form =CourseForm7(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added Successfully!")
            return redirect('year4_first_semester')
    else:
        form = CourseForm7()
    return render(request, 'result/year4_first_semester.html',{'yr4_sem1':yr4_sem1,'form':form})











































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


# ***********************UPLOAD STUDENTS*****************************
def upload_students(request):
    if request.method == 'POST':
        form = StudentFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            try:
                df = pd.read_excel(excel_file)
            except Exception as e:
                messages.error(request, "An error occurred while reading the Excel file.")
                return redirect('student')

            students_added = 0
            students_skipped = 0
            errors = []

            for _, row in df.iterrows():
                fullname = row['fullname']
                email = row['email']
                contact = row['contact']
                gender = row['gender']
                department_name = row['department']
                program_name = row['program']
                dob = row['dob']

                department, _ = Department.objects.get_or_create(department=department_name)
                program, _ = Program.objects.get_or_create(program=program_name, department=department)

                student = Student(
                    fullname=fullname,
                    email=email,
                    contact=contact,
                    gender=gender,
                    department=department,
                    program=program,
                    dob=dob
                )

                try:
                    student.save()
                    students_added += 1
                except Exception as e:
                    errors.append(f"Error creating student '{fullname}': {str(e)}")

            if students_added > 0:
                messages.success(request, f"{students_added} student(s) have been added successfully!")
            if students_skipped > 0:
                messages.warning(request, f"{students_skipped} student(s) already exist and were skipped.")
            if errors:
                messages.error(request, "Some errors occurred while saving students. Please check the error messages.")
                for error in errors:
                    messages.error(request, error)

            return redirect('student')
        else:
            messages.error(request, "Invalid form submission. Please check the form fields.")
            return redirect('student')
    else:
        form = StudentFileForm()

    return render(request, 'result/uploadStudent.html', {'form': form})


























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