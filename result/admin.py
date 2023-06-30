from django.contrib import admin
from .models import Faculty, Department, Program,Courses,Student,ExamsYear,Qualification,Result

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Courses)
admin.site.register(Student)
admin.site.register(ExamsYear)
admin.site.register(Qualification)
admin.site.register(Result)
