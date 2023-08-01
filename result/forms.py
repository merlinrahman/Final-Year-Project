from django.forms import ModelForm
from django import forms
from .models import Faculty,bit_year1_semester1,bit_year4_semester2,bit_year4_semester1,bit_year3_semester1,bit_year3_semester2
from .models import bit_year2_semester1,bit_year2_semester2,bit_year1_semester2, Department, Program, Student,Result,BitResult,MasscomResult
from .models import year1_semester1,year1_semester2,year2_semester1,year2_semester2,year3_semester1,year3_semester2,year4_semester1,year4_semester2
from .models import masscom_year1_semester1,masscom_year1_semester2,masscom_year2_semester1,masscom_year2_semester2,masscom_year3_semester1,masscom_year3_semester2,masscom_year4_semester1,masscom_year4_semester2
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import RegexValidator
from account.models import MyUser

# ===============================EXCEL UPLOADS FORMS================================================
class UniversityFileForm(forms.Form):
    file = forms.FileField()

class UploadFileForm(forms.Form):
    file = forms.FileField()

class CourseFileForm1(forms.Form):
    file = forms.FileField()

class CourseFileForm2(forms.Form):
    file = forms.FileField()

class CourseFileForm3(forms.Form):
    file = forms.FileField()

class CourseFileForm4(forms.Form):
    file = forms.FileField()

class CourseFileForm5(forms.Form):
    file = forms.FileField()

class CourseFileForm6(forms.Form):
    file = forms.FileField()

class CourseFileForm7(forms.Form):
    file = forms.FileField()

class CourseFileForm8(forms.Form):
    file = forms.FileField()
    
class FacultyFileForm(forms.Form):
    file = forms.FileField()

class ProgramFileForm(forms.Form):
    file = forms.FileField()

class StudentFileForm(forms.Form):
    file = forms.FileField()

class BitCourseFileForm(forms.Form):
    file = forms.FileField()

# ********Faculty Form**************
class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['faculty']
        widgets = {
            'faculty': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ***************Department Form*****************
class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['faculty','department']
        widgets = {
            'faculty': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'department': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ***************Program Form*****************
class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ['department', 'program']
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'program': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ****************STUDENTS FORM****************
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fullname','email','contact','gender','department','program','dob']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
            'email': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'contact': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 10000000000000000000000) ? this.value : ''"}),
            'gender': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'department': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'dob': forms.DateInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'YYYY-MM-DD'}),
        }



# =============================================COMPUTER SCIENCE MODULE FORMS==============================
# ********Modules Form**************
class CourseForm1(ModelForm):
    class Meta:
        model = year1_semester1
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class CourseForm2(ModelForm):
    class Meta:
        model = year1_semester2
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }
# ********Modules Form**************
class CourseForm3(ModelForm):
    class Meta:
        model = year2_semester1
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class CourseForm4(ModelForm):
    class Meta:
        model = year2_semester2
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class CourseForm5(ModelForm):
    class Meta:
        model = year3_semester1
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class CourseForm6(ModelForm):
    class Meta:
        model = year3_semester2
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class CourseForm7(ModelForm):
    class Meta:
        model = year4_semester1
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class CourseForm8(ModelForm):
    class Meta:
        model = year4_semester2
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

#*****COMPUTER SCIENCE STUDENTS RESULTS*****
class ResultForm(forms.ModelForm): 
    class Meta:
        model = Result
        fields = [
                  'academicYear','student','department','level','semester','module1','module_grade1','module2', 'module_grade2','module3', 
                  'module_grade3','module4', 'module_grade4','module5','module_grade5','module6', 'module_grade6',

                  'academicYear','level','semester2','semester2_module1','semester2_module_grade1','semester2_module2', 'semester2_module_grade2','semester2_module3', 
                  'semester2_module_grade3','semester2_module4', 'semester2_module_grade4','semester2_module5',
                  'semester2_module_grade5','semester2_module6', 'semester2_module_grade6',

                  'academicYear2','level2','semester3','semester3_module1','semester3_module_grade1','semester3_module2', 'semester3_module_grade2','semester3_module3', 
                  'semester3_module_grade3','semester3_module4', 'semester3_module_grade4','semester3_module5',
                  'semester3_module_grade5','semester3_module6', 'semester3_module_grade6',

                  'academicYear2','level2','semester4','semester4_module1','semester4_module_grade1','semester4_module2', 'semester4_module_grade2','semester4_module3', 
                  'semester4_module_grade3','semester4_module4', 'semester4_module_grade4','semester4_module5',
                  'semester4_module_grade5','semester4_module6', 'semester4_module_grade6',

                  'academicYear3','level3','semester5','semester5_module1','semester5_module_grade1','semester5_module2', 'semester5_module_grade2','semester5_module3', 
                  'semester5_module_grade3','semester5_module4', 'semester5_module_grade4','semester5_module5',
                  'semester5_module_grade5','semester5_module6', 'semester5_module_grade6',

                  'academicYear3','level3','semester6','semester6_module1','semester6_module_grade1','semester6_module2', 'semester6_module_grade2','semester6_module3', 
                  'semester6_module_grade3','semester6_module4', 'semester6_module_grade4','semester6_module5',
                  'semester6_module_grade5','semester6_module6', 'semester6_module_grade6',

                  'academicYear4','level4','semester7','semester7_module1','semester7_module_grade1','semester7_module2', 'semester7_module_grade2','semester7_module3', 
                  'semester7_module_grade3','semester7_module4', 'semester7_module_grade4','semester7_module5',
                  'semester7_module_grade5',

                  'academicYear4','level4','semester8','semester8_module1','semester8_module_grade1','semester8_module2', 'semester8_module_grade2','semester8_module3', 
                  'semester8_module_grade3',
                    ]
        widgets = {
            'academicYear': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'student': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'department': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'module1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'module_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'module2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'module_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'module3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'module_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'module4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'module_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'module5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'module_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'module6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'module_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
    

            
            'academicYear': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_module1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_module_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester2_module2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_module_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester2_module3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_module_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester2_module4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_module_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester2_module5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_module_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester2_module6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_module_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}), 

            'academicYear2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_module1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_module_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester3_module2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_module_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester3_module3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_module_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester3_module4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_module_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester3_module5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_module_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester3_module6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_module_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}), 

            'academicYear2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_module1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_module_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester4_module2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_module_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester4_module3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_module_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester4_module4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_module_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester4_module5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_module_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester4_module6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_module_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),

            'academicYear3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_module1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_module_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester5_module2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_module_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester5_module3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_module_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester5_module4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_module_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester5_module5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_module_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester5_module6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_module_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),

            'academicYear3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_module1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_module_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester6_module2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_module_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester6_module3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_module_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester6_module4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_module_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester6_module5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_module_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester6_module6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_module_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),


            'academicYear4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_module1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_module_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester7_module2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_module_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester7_module3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_module_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester7_module4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_module_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester7_module5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_module_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
           
            'academicYear4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_module1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_module_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester8_module2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_module_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester8_module3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_module_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester8_module4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_module_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester8_module5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_module_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester8_module_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
        }
    





# =========================================BIT MODULE FORM===================================================
# ********Modules Form**************
class BitCourseForm1(ModelForm):
    class Meta:
        model = bit_year1_semester1
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class BitCourseForm2(ModelForm):
    class Meta:
        model = bit_year1_semester2
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }
# ********Modules Form**************
class BitCourseForm3(ModelForm):
    class Meta:
        model = bit_year2_semester1
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class BitCourseForm4(ModelForm):
    class Meta:
        model = bit_year2_semester2
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class BitCourseForm5(ModelForm):
    class Meta:
        model = bit_year3_semester1
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class BitCourseForm6(ModelForm):
    class Meta:
        model = bit_year3_semester2
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class BitCourseForm7(ModelForm):
    class Meta:
        model = bit_year4_semester1
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class BitCourseForm8(ModelForm):
    class Meta:
        model = bit_year4_semester2
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ******BIT STUDENT RESULT FORM******
class BitResultForm(forms.ModelForm): 
    class Meta:
        model = BitResult
        fields = [
                  'academicYear','student','department','level','semester','course1','course_grade1','course2','course_grade2','course3', 
                  'course_grade3','course4','course_grade4','course5','course_grade5','course6','course_grade6',
                  'academicYear','level','semester2','semester2_course1','semester2_course_grade1','semester2_course2','semester2_course_grade2','semester2_course3', 

                  'semester2_course_grade3','semester2_course4','semester2_course_grade4','semester2_course5',
                  'semester2_course_grade5','semester2_course6','semester2_course_grade6',

                  'academicYear2','level2','semester3','semester3_course1','semester3_course_grade1','semester3_course2', 'semester3_course_grade2','semester3_course3', 
                  'semester3_course_grade3','semester3_course4','semester3_course_grade4','semester3_course5',
                  'semester3_course_grade5','semester3_course6','semester3_course_grade6',

                  'academicYear2','level2','semester4','semester4_course1','semester4_course_grade1','semester4_course2','semester4_course_grade2','semester4_course3', 
                  'semester4_course_grade3','semester4_course4','semester4_course_grade4','semester4_course5',
                  'semester4_course_grade5','semester4_course6','semester4_course_grade6',

                  'academicYear3','level3','semester5','semester5_course1','semester5_course_grade1','semester5_course2','semester5_course_grade2','semester5_course3', 
                  'semester5_course_grade3','semester5_course4','semester5_course_grade4','semester5_course5',
                  'semester5_course_grade5','semester5_course6','semester5_course_grade6',

                  'academicYear3','level3','semester6','semester6_course1','semester6_course_grade1','semester6_course2','semester6_course_grade2','semester6_course3', 
                  'semester6_course_grade3','semester6_course4','semester6_course_grade4','semester6_course5',
                  'semester6_course_grade5','semester6_course6','semester6_course_grade6',

                  'academicYear4','level4','semester7','semester7_course1','semester7_course_grade1','semester7_course2','semester7_course_grade2','semester7_course3', 
                  'semester7_course_grade3','semester7_course4','semester7_course_grade4','semester7_course5','semester7_course_grade5',

                  'academicYear4','level4','semester8','semester8_course1','semester8_course_grade1','semester8_course2','semester8_course_grade2','semester8_course3', 
                  'semester8_course_grade3'

                    ]
        widgets = {
            'academicYear': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'student': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'department': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course_grade1': forms.TextInput(attrs={'class':'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'course2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course_grade2': forms.TextInput(attrs={'class':'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'course3': forms.Select(attrs={'class':'form-control shadow-none'}),
            'course_grade3': forms.TextInput(attrs={'class':'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'course4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course_grade4': forms.TextInput(attrs={'class':'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'course5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course_grade5': forms.TextInput(attrs={'class':'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'course6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course_grade6': forms.TextInput(attrs={'class':'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
    

            'academicYear': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_course1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_course_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester2_course2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_course_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester2_course3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_course_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester2_course4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_course_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester2_course5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_course_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester2_course6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_course_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}), 

            'academicYear2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_course1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_course_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester3_course2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_course_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester3_course3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_course_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester3_course4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_course_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester3_course5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_course_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester3_course6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_course_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}), 

            'academicYear2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_course1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_course_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester4_course2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_course_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester4_course3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_course_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester4_course4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_course_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester4_course5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_course_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester4_course6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_course_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),

            'academicYear3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_course1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_course_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester5_course2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_course_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester5_course3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_course_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester5_course4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_course_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester5_course5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_course_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester5_course6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_course_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),

            'academicYear3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_course1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_course_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester6_course2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_course_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester6_course3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_course_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester6_course4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_course_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester6_course5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_course_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester6_course6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_course_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),


            'academicYear4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_course1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_course_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester7_course2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_course_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester7_course3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_course_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester7_course4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_course_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester7_course5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_course_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            


            'academicYear4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_course1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_course_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester8_course2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_course_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester8_course3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_course_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            
         }

   
    

# =========================================MASS COMMUNICATION MODULE FORM===================================================

# ********Modules Form**************
class massCourseForm1(ModelForm):
    class Meta:
        model = masscom_year1_semester1
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class massCourseForm2(ModelForm):
    class Meta:
        model = masscom_year1_semester2
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }
# ********Modules Form**************
class massCourseForm3(ModelForm):
    class Meta:
        model = masscom_year2_semester1
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class massCourseForm4(ModelForm):
    class Meta:
        model = masscom_year2_semester2
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class massCourseForm5(ModelForm):
    class Meta:
        model = masscom_year3_semester1
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class massCourseForm6(ModelForm):
    class Meta:
        model = masscom_year3_semester2
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class massCourseForm7(ModelForm):
    class Meta:
        model = masscom_year4_semester1
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

# ********Modules Form**************
class massCourseForm8(ModelForm):
    class Meta:
        model = masscom_year4_semester2
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z ]/g, '')"}),
        }

class MasscomResultForm(forms.ModelForm): 
    class Meta:
        model = MasscomResult
        fields = [
                  'academicYear','student','department','level','semester','mass_course1','mass_course_grade1','mass_course2','mass_course_grade2','mass_course3', 
                  'mass_course_grade3','mass_course4','mass_course_grade4','mass_course5','mass_course_grade5','mass_course6','mass_course_grade6',
                  'academicYear','level','semester2','semester2_mass_course1','semester2_mass_course_grade1','semester2_mass_course2','semester2_mass_course_grade2','semester2_mass_course3', 

                  'semester2_mass_course_grade3','semester2_mass_course4','semester2_mass_course_grade4','semester2_mass_course5',
                  'semester2_mass_course_grade5','semester2_mass_course6','semester2_mass_course_grade6',

                  'academicYear2','level2','semester3','semester3_mass_course1','semester3_mass_course_grade1','semester3_mass_course2', 'semester3_mass_course_grade2','semester3_mass_course3', 
                  'semester3_mass_course_grade3','semester3_mass_course4','semester3_mass_course_grade4','semester3_mass_course5',
                  'semester3_mass_course_grade5',

                  'academicYear2','level2','semester4','semester4_mass_course1','semester4_mass_course_grade1','semester4_mass_course2','semester4_mass_course_grade2','semester4_mass_course3', 
                  'semester4_mass_course_grade3','semester4_mass_course4','semester4_mass_course_grade4','semester4_mass_course5',
                  'semester4_mass_course_grade5',

                  'academicYear3','level3','semester5','semester5_mass_course1','semester5_mass_course_grade1','semester5_mass_course2','semester5_mass_course_grade2','semester5_mass_course3', 
                  'semester5_mass_course_grade3','semester5_mass_course4','semester5_mass_course_grade4','semester5_mass_course5',
                  'semester5_mass_course_grade5',

                  'academicYear3','level3','semester6','semester6_mass_course1','semester6_mass_course_grade1','semester6_mass_course2','semester6_mass_course_grade2','semester6_mass_course3', 
                  'semester6_mass_course_grade3','semester6_mass_course4','semester6_mass_course_grade4','semester6_mass_course5',
                  'semester6_mass_course_grade5',

                  'academicYear4','level4','semester7','semester7_mass_course1','semester7_mass_course_grade1','semester7_mass_course2','semester7_mass_course_grade2','semester7_mass_course3', 
                  'semester7_mass_course_grade3','semester7_mass_course4','semester7_mass_course_grade4','semester7_mass_course5','semester7_mass_course_grade5',

                  'academicYear4','level4','semester8','semester8_mass_course1','semester8_mass_course_grade1','semester8_mass_course2','semester8_mass_course_grade2','semester8_mass_course3', 
                  'semester8_mass_course_grade3','semester8_mass_course4','semester8_mass_course_grade4'

                    ]
        widgets = {
            'academicYear': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'student': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'department': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'mass_course1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'mass_course_grade1': forms.TextInput(attrs={'class':'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'mass_course2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'mass_course_grade2': forms.TextInput(attrs={'class':'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'mass_course3': forms.Select(attrs={'class':'form-control shadow-none'}),
            'mass_course_grade3': forms.TextInput(attrs={'class':'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'mass_course4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'mass_course_grade4': forms.TextInput(attrs={'class':'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'mass_course5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'mass_course_grade5': forms.TextInput(attrs={'class':'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'mass_course6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'mass_course_grade6': forms.TextInput(attrs={'class':'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
    

            'academicYear': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_mass_course1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_mass_course_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester2_mass_course2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_mass_course_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester2_mass_course3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_mass_course_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester2_mass_course4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_mass_course_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester2_mass_course5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_mass_course_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester2_mass_course6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_mass_course_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}), 

            'academicYear2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_mass_course1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_mass_course_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester3_mass_course2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_mass_course_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester3_mass_course3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_mass_course_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester3_mass_course4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_mass_course_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester3_mass_course5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_mass_course_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            
            'academicYear2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_mass_course1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_mass_course_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester4_mass_course2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_mass_course_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester4_mass_course3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_mass_course_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester4_mass_course4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_mass_course_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester4_mass_course5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_mass_course_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            

            'academicYear3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_mass_course1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_mass_course_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester5_mass_course2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_mass_course_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester5_mass_course3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_mass_course_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester5_mass_course4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_mass_course_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester5_mass_course5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_mass_course_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
           
            'academicYear3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_mass_course1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_mass_course_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester6_mass_course2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_mass_course_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester6_mass_course3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_mass_course_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester6_mass_course4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_mass_course_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester6_mass_course5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_mass_course_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
           


            'academicYear4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_mass_course1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_mass_course_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester7_mass_course2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_mass_course_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester7_mass_course3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_mass_course_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester7_mass_course4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_mass_course_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester7_mass_course5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_mass_course_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            


            'academicYear4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_mass_course1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_mass_course_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester8_mass_course2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_mass_course_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),  
            'semester8_mass_course3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_mass_course_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),
            'semester8_mass_course4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_mass_course_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none','oninput': "this.value = (this.value > 0 && this.value <= 100) ? this.value : ''"}),    
            
         }

