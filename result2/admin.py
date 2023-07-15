from django.contrib import admin
from .models import Njala_Faculty, Njala_Department, Njala_Program,Njala_Student,Njala_ExamsYear
# Register your models here.
admin.site.register(Njala_Faculty)
admin.site.register(Njala_Department)
admin.site.register(Njala_Program)
admin.site.register(Njala_Student)
admin.site.register(Njala_ExamsYear)