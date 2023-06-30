import datetime
from django.db import models
import uuid

GENDER = (
        ('Male','Male'),
        ('Female','Female'),
)

DATE = (
        
        ('2010','2010'),
        ('2011','2011'),
        ('2012','2012'),
        ('2013','2013'),
        ('2014','2014'),
        ('2015','2015'),
        ('2016','2016'),
        ('2017','2017'),
        ('2018','2018'),
        ('2019','2019'),
        ('2020','2020'),
        ('2021','2021'),
        ('2022','2022'),
        ('2023','2023'),
        ('2024','2024'),
        ('2025','2025'),
        ('2026','2026'),
        ('2027','2027'),
        ('2028','2028'),
        ('2029','2029'),
        ('2030','2030'),
)

BATCH = (
        
        ('2010','2010'),
        ('2011','2011'),
        ('2012','2012'),
        ('2013','2013'),
        ('2014','2014'),
        ('2015','2015'),
        ('2016','2016'),
        ('2017','2017'),
        ('2018','2018'),
        ('2019','2019'),
        ('2020','2020'),
        ('2021','2021'),
        ('2022','2022'),
        ('2023','2023'),
        ('2024','2024'),
        ('2025','2025'),
        ('2026','2026'),
        ('2027','2027'),
        ('2028','2028'),
        ('2029','2029'),
        ('2030','2030'),
)

QUALIFICATION = (
        ('Bachelor of Science (BSc)','Bachelor of Science (BSc)'),
        ('Bachelor of Arts (BA)','Bachelor of Arts (BA)'),
        ('Bachelor of Business Administration (BBA)','Bachelor of Business Administration (BBA)'),
        ('Bachelor of Engineering (BEng)','Bachelor of Engineering (BEng)'),
        ('Bachelor of Education (BEd)','Bachelor of Education (BEd)'),
        ('Master of Science (MSc)','Master of Science (MSc)'),
        ('Master of Arts (MA)','Master of Arts (MA)'),
        ('Master of Business Administration (MBA)','Master of Business Administration (MBA)'),
        ('Master of Engineering (MEng)','Master of Engineering (MEng)'),
        ('Master of Education (MEd)','Master of Education (MEd)'),
        ('Diploma in Computer Science','Diploma in Computer Science'),
        ('Diploma in Graphics Design','Diploma in Graphics Design'),
        ('Diploma in Accounting','Diploma in Accounting'),
        ('Diploma in Banking and Finance','Diploma in Banking and Finance'),
        ('HND in Journalism','HND in Journalism'),
        ('HND in Business Administration','HND in Business Administration'),
        ('HND in Radio Broadcasting','HND in Radio Broadcasting'),
        ('HND in Radio English Language','HND in Radio English Language'),
        ('Certificate in Computer Studies','Certificate in Computer Studies'),
        ('Certificate in Project Management','Certificate in Project Management'),
        ('Certificate in Web Development ','Certificate in Web Development '),

)

SEMESTER = (
        
        ('First Semester','First Semester'),
        ('Second Semester','Second Semester'),
       
)

LEVEL = (

        ('First Year','First Year'),
        ('Second Year','Second Year'),
        ('Third Year','Third Year'),
        ('Final Year','Final Year'),
       
)

ACADEMIC_YEAR = (
        
        ('2000/2001','2000/2001'),
        ('2001/2002','2001/2002'),
        ('2002/2003','2002/2003'),
        ('2003/2004','2003/2004'),
        ('2004/2005','2004/2005'),
        ('2005/2006','2005/2006'),
        ('2006/2007','2006/2007'),
        ('2007/2008','2007/2008'),
        ('2008/2009','2008/2009'),
        ('2009/2010','2009/2010'),
        ('2010/2011','2010/2011'),
        ('2011/2012','2011/2012'),
        ('2012/2013','2012/2013'),
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

# class University(models.Model):
#     university = models.CharField(max_length=100)
#     uni_number = models.CharField(max_length=20)
#     def __str__(self):
#         return self.university
    
class ExamsYear(models.Model):
    academicyear= models.CharField(max_length=20, choices=ACADEMIC_YEAR)
    
        

class Qualification(models.Model):
    qualification = models.CharField(max_length=100, choices=QUALIFICATION)
    

    # ****FACULTY******
class Faculty(models.Model):
    faculty = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.faculty


     # ****DEPARTMENT******
class Department(models.Model):
    department = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    def __str__(self):
        return self.department
    

        # ****PROGRAMS******
class Program(models.Model):
    program = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.program
    


     # ****COURSES/MODULES******
class Courses(models.Model):
    code = models.CharField(max_length=50, unique=True, default='')
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.course
    



     # ********STUDENTS******


class Student(models.Model):
        student_id = models.CharField(max_length=50, unique=True)
        fullname = models.CharField(max_length=100)
        gender = models.TextField(max_length=20, choices=GENDER)
        department = models.ForeignKey(Department, on_delete=models.CASCADE)
        program = models.ForeignKey(Program, on_delete=models.CASCADE)
        level = models.TextField(max_length=50, choices=LEVEL)
        dob = models.DateField(null=True)

        def __str__(self):
            return self.fullname

        def save(self, *args, **kwargs):
            if not self.student_id:
                # Generate your custom ID here, e.g., using a combination of fields
                # For example, using the first 3 characters of the fullname and the last 4 digits of the current year
                self.student_id = self.fullname[:3].upper() + str(datetime.date.today().year)[-4:]
                
                # You can add additional logic to ensure uniqueness if necessary
                
            super().save(*args, **kwargs)



        


class Result(models.Model):
    entry_date = models.DateTimeField(auto_now_add=True, null=True)
    academicYear = models.TextField(max_length=20, choices=ACADEMIC_YEAR)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    module1 = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='module1_results')
    module2 = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='module2_results')
    module3 = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='module3_results')
    module4 = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='module4_results')
    module5 = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='module5_results')
    module6 = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='module6_results')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    level = models.TextField(max_length=50, choices=LEVEL)
    semester = models.TextField(max_length=50, choices=SEMESTER)
    module_grade1 = models.IntegerField()
    module_grade2 = models.IntegerField()
    module_grade3 = models.IntegerField()
    module_grade4 = models.IntegerField()
    module_grade5 = models.IntegerField()
    module_grade6 = models.IntegerField()
    gradepoint1 = models.TextField(max_length=2)
    gradepoint2 = models.TextField(max_length=2)
    gradepoint3 = models.TextField(max_length=2)
    gradepoint4 = models.TextField(max_length=2)
    gradepoint5 = models.TextField(max_length=2)
    gradepoint6 = models.TextField(max_length=2)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sgp = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sgpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sch = models.IntegerField(null=True, default=3)
    totalsch = models.IntegerField(null=True, default=0)
    equivalent1 = models.IntegerField(null=True, default=0)
    equivalent2 = models.IntegerField(null=True, default=0)
    equivalent3 = models.IntegerField(null=True, default=0)
    equivalent4 = models.IntegerField(null=True, default=0)
    equivalent5 = models.IntegerField(null=True, default=0)
    equivalent6 = models.IntegerField(null=True, default=0)
    grade1 = models.CharField(max_length=1, blank=True, null=True)
    grade2 = models.CharField(max_length=1, blank=True, null=True)
    grade3 = models.CharField(max_length=1, blank=True, null=True)
    grade4 = models.CharField(max_length=1, blank=True, null=True)
    grade5 = models.CharField(max_length=1, blank=True, null=True)
    grade6 = models.CharField(max_length=1, blank=True, null=True)
   
    def save(self, *args, **kwargs):
        if self.module_grade1 >= 75:
            self.equivalent1 = 5
            self.grade1 = 'A'
        elif self.module_grade1 >= 65:
            self.equivalent1 = 4
            self.grade1 = 'B'
        elif self.module_grade1 >= 50:
            self.equivalent1 = 3
            self.grade1 = 'C'
        elif self.module_grade1 >= 35:
            self.equivalent1 = 2
            self.grade1 = 'D'
        elif self.module_grade1 >= 20:
            self.equivalent1 = 1
            self.grade1 = 'E'
        else:
            self.equivalent1 = 0
            self.grade1 = 'F'
        self.gradepoint1 = self.equivalent1 * 3
            
         

        if self.module_grade2 >= 75:
            self.equivalent2 = 5
            self.grade2 = 'A'
        elif self.module_grade2 >= 65:
            self.equivalent2 = 4
            self.grade2 = 'B'
        elif self.module_grade2 >= 50:
            self.equivalent2 = 3
            self.grade2 = 'C'
        elif self.module_grade2 >= 35:
            self.equivalent2 = 2
            self.grade2 = 'D'
        elif self.module_grade2 >= 20:
            self.equivalent2 = 1
            self.grade2 = 'E'
        else:
            self.equivalent2 = 0
            self.grade2 = 'F'
        self.gradepoint2 = self.equivalent2 * 3




        if self.module_grade3 >= 75:
            self.equivalent3 = 5
            self.grade3 = 'A'
        elif self.module_grade3 >= 65:
            self.equivalent3 = 4
            self.grade3 = 'B'
        elif self.module_grade3 >= 50:
            self.equivalent3 = 3
            self.grade3 = 'C'
        elif self.module_grade3 >= 35:
            self.equivalent3 = 2
            self.grade3 = 'D'
        elif self.module_grade3 >= 20:
            self.equivalent3 = 1
            self.grade3 = 'E'
        else:
            self.equivalent3 = 0
            self.grade3 = 'F'
        self.gradepoint3 = self.equivalent3 * 3



        if self.module_grade4 >= 75:
            self.equivalent4 = 5
            self.grade4 = 'A'
        elif self.module_grade4 >= 65:
            self.equivalent4 = 4
            self.grade4 = 'B'
        elif self.module_grade4 >= 50:
            self.equivalent4 = 3
            self.grade4 = 'C'
        elif self.module_grade4 >= 35:
            self.equivalent4 = 2
            self.grade4 = 'D'
        elif self.module_grade4 >= 20:
            self.equivalent4 = 1
            self.grade4 = 'E'
        else:
            self.equivalent4 = 0
            self.grade4 = 'F'
        self.gradepoint4 = self.equivalent4 * 3



        if self.module_grade5 >= 75:
            self.equivalent5 = 5
            self.grade5 = 'A'
        elif self.module_grade5 >= 65:
            self.equivalent5 = 4
            self.grade5 = 'B'
        elif self.module_grade5 >= 50:
            self.equivalent5 = 3
            self.grade5 = 'C'
        elif self.module_grade5 >= 35:
            self.equivalent5 = 2
            self.grade5 = 'D'
        elif self.module_grade5 >= 20:
            self.equivalent5 = 1
            self.grade5 = 'E'
        else:
            self.equivalent5 = 0
            self.grade5 = 'F'
        self.gradepoint5 = self.equivalent5 * 3




        if self.module_grade6 >= 75:
            self.equivalent6 = 5
            self.grade6 = 'A'
        elif self.module_grade6 >= 65:
            self.equivalent6 = 4
            self.grade6 = 'B'
        elif self.module_grade6 >= 50:
            self.equivalent6 = 3
            self.grade6 = 'C'
        elif self.module_grade6 >= 35:
            self.equivalent6 = 2
            self.grade6 = 'D'
        elif self.module_grade6 >= 20:
            self.equivalent6 = 1
            self.grade6 = 'E'
        else:
            self.equivalent6 = 0
            self.grade6 = 'F'
        self.gradepoint6 = self.equivalent6 * 3

        self.totalsch = self.sch + self.sch + self.sch + self.sch  + self.sch  + self.sch
        self.sgp = int(self.gradepoint1) + int(self.gradepoint2) + int(self.gradepoint3) + int(self.gradepoint4) + int(self.gradepoint5) + int(self.gradepoint6) 
        self.sgpa = self.sgp / self.totalsch

        # Save the result
        super(Result, self).save(*args, **kwargs)

    def __str__(self):
        return f'This is the result for {self.student} for - {self.semester}'