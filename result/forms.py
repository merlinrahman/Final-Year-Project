from django.forms import ModelForm
from django import forms
from .models import Faculty, Department, Program, Courses, Student,Result
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import inlineformset_factory

# =====INLINE FORMSET=======
from django.forms import inlineformset_factory


from account.models import MyUser

# ********Excel uploads*********

class UniversityFileForm(forms.Form):
    file = forms.FileField()

class UploadFileForm(forms.Form):
    file = forms.FileField()


class CourseFileForm(forms.Form):
    file = forms.FileField()


class FacultyFileForm(forms.Form):
    file = forms.FileField()




class ProgramFileForm(forms.Form):
    file = forms.FileField()







# ********Faculty Form**************
class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = ['faculty']
        widgets = {
            # 'university': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'faculty': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
        }


# ***************Department Form*****************
class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['faculty', 'department']
        widgets = {
            'faculty': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'department': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
        }


# ***************Program Form*****************
class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ['department', 'program']
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'program': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
        }



# ********Modules Form**************
class CourseForm(ModelForm):
    class Meta:
        model = Courses
        fields = ['code','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
        }







class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fullname','gender','department','program','level','dob']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'gender': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'department': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'dob': forms.DateInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'YYYY-MM-DD'}),
        }











class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['academicYear','student','department','level','semester','module1', 
                  'module_grade1','module2', 'module_grade2','module3', 
                  'module_grade3','module4', 'module_grade4','module5',
                    'module_grade5','module6', 'module_grade6']
        widgets = {
            'academicYear': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'student': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'department': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'module1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'module_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'module2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'module_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'module3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'module_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'module4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'module_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'module5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'module_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'module6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'module_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
        }

    

