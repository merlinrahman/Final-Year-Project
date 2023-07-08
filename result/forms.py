from django.forms import ModelForm
from django import forms
from .models import Faculty, Department, Program, Student,Result,year1_semester1,year1_semester2,year2_semester1,year2_semester2,year3_semester1,year3_semester2,year4_semester1,year4_semester2
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

class CourseFileForm(forms.Form):
    file = forms.FileField()


class FacultyFileForm(forms.Form):
    file = forms.FileField()


class ProgramFileForm(forms.Form):
    file = forms.FileField()

class StudentFileForm(forms.Form):
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
class CourseForm1(ModelForm):
    class Meta:
        model = year1_semester1
        fields = ['code','program','level','semester','course']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
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
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
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
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
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
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
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
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
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
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
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
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
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
            'course': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
        }





class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fullname','email','contact','gender','department','program','dob']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'email': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'contact': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'gender': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'department': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'program': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'dob': forms.DateInput(attrs={'class': 'form-control shadow-none', 'placeholder': 'YYYY-MM-DD'}),
        }











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
                  'semester7_module_grade5','semester7_module6', 'semester7_module_grade6',

                  'academicYear4','level4','semester8','semester8_module1','semester8_module_grade1','semester8_module2', 'semester8_module_grade2','semester8_module3', 
                  'semester8_module_grade3','semester8_module4', 'semester8_module_grade4','semester8_module5',
                  'semester8_module_grade5','semester8_module6', 'semester8_module_grade6',

                    ]
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

            
            'academicYear': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_module1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_module_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'semester2_module2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_module_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester2_module3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_module_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester2_module4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_module_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester2_module5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_module_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester2_module6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester2_module_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none'}), 

            'academicYear2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_module1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_module_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'semester3_module2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_module_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester3_module3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_module_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester3_module4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_module_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester3_module5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_module_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester3_module6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester3_module_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none'}), 

            'academicYear2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_module1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_module_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'semester4_module2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_module_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester4_module3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_module_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester4_module4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_module_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester4_module5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_module_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester4_module6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester4_module_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none'}),

            'academicYear3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_module1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_module_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'semester5_module2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_module_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester5_module3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_module_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester5_module4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_module_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester5_module5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_module_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester5_module6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester5_module_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none'}),

            'academicYear3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_module1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_module_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'semester6_module2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_module_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester6_module3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_module_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester6_module4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_module_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester6_module5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_module_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester6_module6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester6_module_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none'}),


            'academicYear4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_module1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_module_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'semester7_module2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_module_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester7_module3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_module_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester7_module4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_module_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester7_module5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_module_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester7_module6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester7_module_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none'}), 


            'academicYear4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'level4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_module1': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_module_grade1': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'semester8_module2': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_module_grade2': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester8_module3': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_module_grade3': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester8_module4': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_module_grade4': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester8_module5': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_module_grade5': forms.TextInput(attrs={'class': 'form-control shadow-none'}),  
            'semester8_module6': forms.Select(attrs={'class': 'form-control shadow-none'}),
            'semester8_module_grade6': forms.TextInput(attrs={'class': 'form-control shadow-none'}), 
        }

    

