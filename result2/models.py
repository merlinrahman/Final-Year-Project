from django.core.validators import RegexValidator
import datetime
from django.db import models
import uuid
import random
import string


ACADEMIC_YEAR = (

        ('2014/2015','2014/2015'),
        ('2015/2016','2015/2016'),
        ('2016/2017','2016/2017'),
        ('2017/2018','2017/2018'),
        ('2018/2019','2018/2019'),
        ('2019/2020','2019/2020'),
        ('2020/2021','2020/2021'),
        ('2021/2022','2021/2022'),
        ('2022/2023','2022/2023'),  
)


YEAR2_ACADEMIC_YEAR = (
    
       
        ('2014/2015','2014/2015'),
        ('2015/2016','2015/2016'),
        ('2016/2017','2016/2017'),
        ('2017/2018','2017/2018'),
        ('2018/2019','2018/2019'),
        ('2019/2020','2019/2020'),
        ('2020/2021','2020/2021'),
        ('2021/2022','2021/2022'),
        ('2022/2023','2022/2023'),  
)

YEAR3_ACADEMIC_YEAR = (
    
        
        ('2013/2014','2013/2014'),
        ('2014/2015','2014/2015'),
        ('2015/2016','2015/2016'),
        ('2016/2017','2016/2017'),
        ('2017/2018','2017/2018'),
        ('2018/2019','2018/2019'),
        ('2019/2020','2019/2020'),
        ('2020/2021','2020/2021'),
        ('2021/2022','2021/2022'),
        ('2022/2023','2022/2023'),  
)

YEAR4_ACADEMIC_YEAR = (
        ('2013/2014','2013/2014'),
        ('2014/2015','2014/2015'),
        ('2015/2016','2015/2016'),
        ('2016/2017','2016/2017'),
        ('2017/2018','2017/2018'),
        ('2018/2019','2018/2019'),
        ('2019/2020','2019/2020'),
        ('2020/2021','2020/2021'),
        ('2021/2022','2021/2022'),
        ('2022/2023','2022/2023'),  
)



GENDER = (
        ('Male','Male'),
        ('Female','Female'),
)
# Create your models here.
class Njala_ExamsYear(models.Model):
    academicyear= models.CharField(max_length=20, choices=ACADEMIC_YEAR)
    

    # ****FACULTY******
class Njala_Faculty(models.Model):
    faculty = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.faculty


     # ****DEPARTMENT******
class Njala_Department(models.Model):
    department = models.CharField(max_length=100)
    faculty = models.ForeignKey(Njala_Faculty, on_delete=models.CASCADE)
    def __str__(self):
        return self.department
    

        # ****PROGRAMS******
class Njala_Program(models.Model):
    program = models.CharField(max_length=100)
    department = models.ForeignKey(Njala_Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.program
class Njala_Student(models.Model):
    student_id = models.CharField(max_length=50, unique=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    contact = models.CharField(max_length=15)
    gender = models.TextField(max_length=20, choices=GENDER)
    department = models.ForeignKey(Njala_Department, on_delete=models.CASCADE)
    program = models.ForeignKey(Njala_Program, on_delete=models.CASCADE)
    dob = models.DateField(null=True)

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        if not self.student_id:
            random_numbers = ''.join(random.choices(string.digits, k=5))
            self.student_id = 'cusl' + random_numbers
            
            # You can add additional logic to ensure uniqueness if necessary
            
        super().save(*args, **kwargs)
