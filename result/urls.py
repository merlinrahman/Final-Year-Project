from django.urls import path, include
from . import views


urlpatterns = [

              # LOGIN-REGISTER PAGE
    #***************************************
    path('login_register/', views.login_register, name='login_register'),



    # CUSL HOME PAGE
    #***************************************
    path('cusl_home/', views.cusl_home, name='cusl_home'),

  

    # # ***************************************
    #              # ADMIN1
    # #*****************************************
    path('admin1/', views.admin1, name='admin1'),
  

     # ***************************************
                 # STUDENT LOGIN
    #*****************************************
    path('login/', views.login, name='login'),



     # ***************************************
                 # STUDENT REGISTER
    #*****************************************
    path('register/', views.register, name='register'),

    
    # ***************************************
                 # STUDENT LOGIN
    #*****************************************
    path('student_login/', views.student_login, name='student_login'),


        
    # ***************************************
                 # STUDENT LOGOUT
    #*****************************************
    path('student_logout/', views.student_logout, name='student_logout'),


        # ***************************************
                 # EXAMS OFFICER LOGIN
    #*****************************************
    path('admin_login/', views.admin_login, name='admin_login'),

    #***************ADMIN LOGIN***************8
    path('admin-redirect/', views.admin_redirect, name='admin_redirect'),


    
    
                 # FACULTIES
    #*****************************************
    path('faculty/', views.faculty, name='faculty'), #create and list all faculties
    path('delete_faculty/<int:pk>/', views.delete_faculty, name='delete_faculty'), #delete faculty
    path('edit_faculty/<int:pk>/', views.edit_faculty, name='edit_faculty'), #edit faculty
    path('view_faculty/<int:pk>/', views.view_faculty, name='view_faculty'), #view faculty
    path('upload_faculty/', views.upload_faculty, name='upload_faculty'),
   
    

    # ***************************************
                 # DEPARTMENTS
    #*****************************************
     path('department/', views.department, name='department'),
     path('delete_department/<int:pk>/', views.delete_department, name='delete_department'), 
     path('edit_department/<int:pk>/', views.edit_department, name='edit_department'), #edit faculty
     path('view_department/<int:pk>/', views.view_department, name='view_department'), #view faculty
     path('upload/', views.upload_file, name='upload_file'),



     # ***************************************
                 # PROGRAMS
    #*****************************************
    path('programs/', views.programs, name='programs'),
    path('edit_program/<int:pk>/', views.edit_program, name='edit_program'),
    path('delete_program/<int:pk>/', views.delete_program, name='delete_program'), 
    path('view_program/<int:pk>/', views.view_program, name='view_program'),
    path('upload_programs/', views.upload_programs, name='upload_programs'),

   # ***************************************
                 #  STUDENTS
    #*****************************************
    path('student/', views.student, name='student'),
    path('edit_student/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'), 
    path('view_student/<int:pk>/', views.view_student, name='view_student'),
    path('upload_students/', views.upload_students, name='upload_students'),




    # ***************************************
                 # COMPUTER SCIENCE STUDENTS RESULTS
    #*****************************************
    path('result/', views.result, name='result'),
    path('edit_result/<int:pk>/', views.edit_result, name='edit_result'),
    path('delete_result/<int:pk>/', views.delete_result, name='delete_result'), 
    path('view_result/<int:pk>/', views.view_result, name='view_result'),
    

     # ***************************************
                 # BIT  STUDENTS RESULTS
    #*****************************************
    path('bit/', views.bit, name='bit'),
    path('bit_result/', views.bit_result, name='bit_result'),
    # path('edit_bit_result/<int:pk>/', views.edit_bit_result, name='edit_bit_result'),
    # path('delete_bit_result/<int:pk>/', views.delete_bit_result, name='delete_bit_result'), 
    # path('view_bit_result/<int:pk>/', views.view_bit_result, name='view_bit_result'),
    


    # ***************************************
                 # MASSCOM  STUDENTS RESULTS
    #*****************************************
    path('masscom/', views.masscom, name='masscom'),
    # path('edit_bit_result/<int:pk>/', views.edit_bit_result, name='edit_bit_result'),
    # path('delete_bit_result/<int:pk>/', views.delete_bit_result, name='delete_bit_result'), 
    # path('view_bit_result/<int:pk>/', views.view_bit_result, name='view_bit_result'),


     # ***************************************
                 #  Searching for result
    #*****************************************
    path('search_result/', views.search_result, name='search_result'),
    path('view_student_result/<str:email>/<str:id_number>/', views.view_student_result, name='view_student_result'),
    



    



    #===============================================================================================================
                                     #COMPUTER SCIENCE courseS/COURSES
    #===============================================================================================================

    # ***************************************
                 # YEAR 1 SEMESTER 1
    #*****************************************
    path('year1_first_semester/', views.year1_first_semester, name='year1_first_semester'),
    path('edit_year1_first_semester/<int:pk>/', views.edit_year1_first_semester, name='edit_year1_first_semester'),
    path('delete_year1_first_semester/<int:pk>/', views.delete_year1_first_semester, name='delete_year1_first_semester'), 
    path('view_year1_first_semester/<int:pk>/', views.view_year1_first_semester, name='view_year1_first_semester'),
    path('upload_course/', views.upload_course, name='upload_course'),


    # ***************************************
                 # YEAR 1 SEMESTER 2
    #*****************************************
    path('year1_second_semester/', views.year1_second_semester, name='year1_second_semester'),
    path('edit_year1_second_semester/<int:pk>/', views.edit_year1_second_semester, name='edit_year1_second_semester'),
    path('delete_year1_second_semester/<int:pk>/', views.delete_year1_second_semester, name='delete_year1_second_semester'), 
    path('view_year1_second_semester/<int:pk>/', views.view_year1_second_semester, name='view_year1_second_semester'),
    path('upload_course2/', views.upload_course2, name='upload_course2'),


    # ***************************************
                 # YEAR 2 SEMESTER 1
    #*****************************************
    path('year2_first_semester/', views.year2_first_semester, name='year2_first_semester'),
    path('edit_year2_first_semester/<int:pk>/', views.edit_year2_first_semester, name='edit_year2_first_semester'),
    path('delete_year2_first_semester/<int:pk>/', views.delete_year2_first_semester, name='delete_year2_first_semester'), 
    path('view_year2_first_semester/<int:pk>/', views.view_year2_first_semester, name='view_year2_first_semester'),
    path('upload_course3/', views.upload_course3, name='upload_course3'),

     # ***************************************
                 # YEAR 2 SEMESTER 2
    #*****************************************
    path('year2_second_semester/', views.year2_second_semester, name='year2_second_semester'),
    path('edit_year2_second_semester/<int:pk>/', views.edit_year2_second_semester, name='edit_year2_second_semester'),
    path('delete_year2_second_semester/<int:pk>/', views.delete_year2_second_semester, name='delete_year2_second_semester'), 
    path('view_year2_second_semester/<int:pk>/', views.view_year2_second_semester, name='view_year2_second_semester'),
    path('upload_course4/', views.upload_course4, name='upload_course4'),


    # ***************************************
                 #  YEAR 3 SEMESTER 1
    #*****************************************
    path('year3_first_semester/', views.year3_first_semester, name='year3_first_semester'),
    path('edit_year3_first_semester/<int:pk>/', views.edit_year3_first_semester, name='edit_year3_first_semester'),
    path('delete_year3_first_semester/<int:pk>/', views.delete_year3_first_semester, name='delete_year3_first_semester'), 
    path('view_year3_first_semester/<int:pk>/', views.view_year3_first_semester, name='view_year3_first_semester'),
    path('upload_course5/', views.upload_course5, name='upload_course5'),

    # ***************************************
                 #  YEAR 3 SEMESTER 2
    #*****************************************
    path('year3_second_semester/', views.year3_second_semester, name='year3_second_semester'),
    path('edit_year3_second_semester/<int:pk>/', views.edit_year3_second_semester, name='edit_year3_second_semester'),
    path('delete_year3_second_semester/<int:pk>/', views.delete_year3_second_semester, name='delete_year3_second_semester'), 
    path('view_year3_second_semester/<int:pk>/', views.view_year3_second_semester, name='view_year3_second_semester'),
    path('upload_course6/', views.upload_course6, name='upload_course6'),

     # ***************************************
                #  YEAR 4 SEMESTER 1
    #*****************************************
    path('year4_first_semester/', views.year4_first_semester, name='year4_first_semester'),
    path('edit_year4_first_semester/<int:pk>/', views.edit_year4_first_semester, name='edit_year4_first_semester'),
    path('delete_year4_first_semester/<int:pk>/', views.delete_year4_first_semester, name='delete_year4_first_semester'), 
    path('view_year4_first_semester/<int:pk>/', views.view_year4_first_semester, name='view_year4_first_semester'),
    path('upload_course7/', views.upload_course7, name='upload_course7'),


     # ***************************************
                 #  YEAR 4 SEMESTER 2
    #*****************************************
    path('year4_second_semester/', views.year4_second_semester, name='year4_second_semester'),
    path('edit_year4_second_semester/<int:pk>/', views.edit_year4_second_semester, name='edit_year4_second_semester'),
    path('delete_year4_second_semester/<int:pk>/', views.delete_year4_second_semester, name='delete_year4_second_semester'), 
    path('view_year4_second_semester/<int:pk>/', views.view_year4_second_semester, name='view_year4_second_semester'),
    path('upload_course8/', views.upload_course8, name='upload_course8'),








    #===============================================================================================================
                                     #B.I.T courseS/COURSES
    #===============================================================================================================
      # ***************************************
                 # YEAR 1 SEMESTER 1
    #*****************************************
    path('bit_year1_first_semester/', views.bit_year1_first_semester, name='bit_year1_first_semester'),
    path('edit_bit_year1_first_semester/<int:pk>/', views.edit_bit_year1_first_semester, name='edit_bit_year1_first_semester'),
    path('delete_bit_year1_first_semester/<int:pk>/', views.delete_bit_year1_first_semester, name='delete_bit_year1_first_semester'), 
    path('view_bit_year1_first_semester/<int:pk>/', views.view_bit_year1_first_semester, name='view_bit_year1_first_semester'),
    path('upload_bit_course1/', views.upload_bit_course1, name='upload_bit_course1'),


     # ***************************************
                 # YEAR 1 SEMESTER 2
    #*****************************************
    path('bit_year1_second_semester/', views.bit_year1_second_semester, name='bit_year1_second_semester'),
    path('edit_bit_year1_second_semester/<int:pk>/', views.edit_bit_year1_second_semester, name='edit_bit_year1_second_semester'),
    path('delete_bit_year1_second_semester/<int:pk>/', views.delete_bit_year1_second_semester, name='delete_bit_year1_second_semester'), 
    path('view_bit_year1_second_semester/<int:pk>/', views.view_bit_year1_second_semester, name='view_bit_year1_second_semester'),
    path('upload_bit_course2/', views.upload_bit_course2, name='upload_bit_course2'),



     # ***************************************
                 # YEAR 2 SEMESTER 1
    #*****************************************
    path('bit_year2_first_semester/', views.bit_year2_first_semester, name='bit_year2_first_semester'),
    path('edit_bit_year2_first_semester/<int:pk>/', views.edit_bit_year2_first_semester, name='edit_bit_year2_first_semester'),
    path('delete_bit_year2_first_semester/<int:pk>/', views.delete_bit_year2_first_semester, name='delete_bit_year2_first_semester'), 
    path('view_bit_year2_first_semester/<int:pk>/', views.view_bit_year2_first_semester, name='view_bit_year2_first_semester'),
    path('upload_bit_course3/', views.upload_bit_course3, name='upload_bit_course3'),

     # ***************************************
                 # YEAR 2 SEMESTER 2
    #*****************************************
    path('bit_year2_second_semester/', views.bit_year2_second_semester, name='bit_year2_second_semester'),
    path('edit_bit_year2_second_semester/<int:pk>/', views.edit_bit_year2_second_semester, name='edit_bit_year2_second_semester'),
    path('delete_bit_year2_second_semester/<int:pk>/', views.delete_bit_year2_second_semester, name='delete_bit_year2_second_semester'), 
    path('view_bit_year2_second_semester/<int:pk>/', views.view_bit_year2_second_semester, name='view_bit_year2_second_semester'),
    path('upload_bit_course4/', views.upload_bit_course4, name='upload_bit_course4'),

     # ***************************************
                 # YEAR 3 SEMESTER 1
    #*****************************************
    path('bit_year3_first_semester/', views.bit_year3_first_semester, name='bit_year3_first_semester'),
    path('edit_bit_year3_first_semester/<int:pk>/', views.edit_bit_year3_first_semester, name='edit_bit_year3_first_semester'),
    path('delete_bit_year3_first_semester/<int:pk>/', views.delete_bit_year3_first_semester, name='delete_bit_year3_first_semester'), 
    path('view_bit_year3_first_semester/<int:pk>/', views.view_bit_year3_first_semester, name='view_bit_year3_first_semester'),
    path('upload_bit_course5/', views.upload_bit_course5, name='upload_bit_course5'),

     # ***************************************
                 # YEAR 3 SEMESTER 2
    #*****************************************
    path('bit_year3_second_semester/', views.bit_year3_second_semester, name='bit_year3_second_semester'),
    path('edit_bit_year3_second_semester/<int:pk>/', views.edit_bit_year3_second_semester, name='edit_bit_year3_second_semester'),
    path('delete_bit_year3_second_semester/<int:pk>/', views.delete_bit_year3_second_semester, name='delete_bit_year3_second_semester'), 
    path('view_bit_year3_second_semester/<int:pk>/', views.view_bit_year3_second_semester, name='view_bit_year3_second_semester'),
    path('upload_bit_course6/', views.upload_bit_course6, name='upload_bit_course6'),

     # ***************************************
                 # YEAR 4 SEMESTER 1
    #*****************************************
    path('bit_year4_first_semester/', views.bit_year4_first_semester, name='bit_year4_first_semester'),
    path('edit_bit_year4_first_semester/<int:pk>/', views.edit_bit_year4_first_semester, name='edit_bit_year4_first_semester'),
    path('delete_bit_year4_first_semester/<int:pk>/', views.delete_bit_year4_first_semester, name='delete_bit_year4_first_semester'), 
    path('view_bit_year4_first_semester/<int:pk>/', views.view_bit_year4_first_semester, name='view_bit_year4_first_semester'),
    path('upload_bit_course7/', views.upload_bit_course7, name='upload_bit_course7'),


     # ***************************************
                 # YEAR 4 SEMESTER 2
    #*****************************************
    path('bit_year4_second_semester/', views.bit_year4_second_semester, name='bit_year4_second_semester'),
    path('edit_bit_year4_second_semester/<int:pk>/', views.edit_bit_year4_second_semester, name='edit_bit_year4_second_semester'),
    path('delete_bit_year4_second_semester/<int:pk>/', views.delete_bit_year4_second_semester, name='delete_bit_year4_second_semester'), 
    path('view_bit_year4_second_semester/<int:pk>/', views.view_bit_year4_second_semester, name='view_bit_year4_second_semester'),
    path('upload_bit_course8/', views.upload_bit_course8, name='upload_bit_course8'),
    



     #===============================================================================================================
                                     #MASS COMMUNICATION courseS/COURSES
    #===============================================================================================================
      # ***************************************
                 # YEAR 1 SEMESTER 1
    #*****************************************
    path('masscom_year1_first_semester/', views.masscom_year1_first_semester, name='masscom_year1_first_semester'),
    path('edit_masscom_year1_first_semester/<int:pk>/', views.edit_masscom_year1_first_semester, name='edit_masscom_year1_first_semester'),
    path('delete_masscom_year1_first_semester/<int:pk>/', views.delete_masscom_year1_first_semester, name='delete_masscom_year1_first_semester'), 
    path('view_masscom_year1_first_semester/<int:pk>/', views.view_masscom_year1_first_semester, name='view_masscom_year1_first_semester'),
    path('upload_masscom_course1/', views.upload_masscom_course1, name='upload_masscom_course1'),


     # ***************************************
                 # YEAR 1 SEMESTER 2
    #*****************************************
    path('masscom_year1_second_semester/', views.masscom_year1_second_semester, name='masscom_year1_second_semester'),
    path('edit_masscom_year1_second_semester/<int:pk>/', views.edit_masscom_year1_second_semester, name='edit_masscom_year1_second_semester'),
    path('delete_masscom_year1_second_semester/<int:pk>/', views.delete_masscom_year1_second_semester, name='delete_masscom_year1_second_semester'), 
    path('view_masscom_year1_second_semester/<int:pk>/', views.view_masscom_year1_second_semester, name='view_masscom_year1_second_semester'),
    path('upload_masscom_course2/', views.upload_masscom_course2, name='upload_masscom_course2'),



     # ***************************************
                 # YEAR 2 SEMESTER 1
    #*****************************************
    path('masscom_year2_first_semester/', views.masscom_year2_first_semester, name='masscom_year2_first_semester'),
    path('edit_masscom_year2_first_semester/<int:pk>/', views.edit_masscom_year2_first_semester, name='edit_masscom_year2_first_semester'),
    path('delete_masscom_year2_first_semester/<int:pk>/', views.delete_masscom_year2_first_semester, name='delete_masscom_year2_first_semester'), 
    path('view_masscom_year2_first_semester/<int:pk>/', views.view_masscom_year2_first_semester, name='view_masscom_year2_first_semester'),
    path('upload_masscom_course3/', views.upload_masscom_course3, name='upload_masscom_course3'),

     # ***************************************
                 # YEAR 2 SEMESTER 2
    #*****************************************
    path('masscom_year2_second_semester/', views.masscom_year2_second_semester, name='masscom_year2_second_semester'),
    path('edit_masscom_year2_second_semester/<int:pk>/', views.edit_masscom_year2_second_semester, name='edit_masscom_year2_second_semester'),
    path('delete_masscom_year2_second_semester/<int:pk>/', views.delete_masscom_year2_second_semester, name='delete_masscom_year2_second_semester'), 
    path('view_masscom_year2_second_semester/<int:pk>/', views.view_masscom_year2_second_semester, name='view_masscom_year2_second_semester'),
    path('upload_masscom_course4/', views.upload_masscom_course4, name='upload_masscom_course4'),

     # ***************************************
                 # YEAR 3 SEMESTER 1
    #*****************************************
    path('masscom_year3_first_semester/', views.masscom_year3_first_semester, name='masscom_year3_first_semester'),
    path('edit_masscom_year3_first_semester/<int:pk>/', views.edit_masscom_year3_first_semester, name='edit_masscom_year3_first_semester'),
    path('delete_masscom_year3_first_semester/<int:pk>/', views.delete_masscom_year3_first_semester, name='delete_masscom_year3_first_semester'), 
    path('view_masscom_year3_first_semester/<int:pk>/', views.view_masscom_year3_first_semester, name='view_masscom_year3_first_semester'),
    path('upload_masscom_course5/', views.upload_masscom_course5, name='upload_masscom_course5'),

     # ***************************************
                 # YEAR 3 SEMESTER 2
    #*****************************************
    path('masscom_year3_second_semester/', views.masscom_year3_second_semester, name='masscom_year3_second_semester'),
    path('edit_masscom_year3_second_semester/<int:pk>/', views.edit_masscom_year3_second_semester, name='edit_masscom_year3_second_semester'),
    path('delete_masscom_year3_second_semester/<int:pk>/', views.delete_masscom_year3_second_semester, name='delete_masscom_year3_second_semester'), 
    path('view_masscom_year3_second_semester/<int:pk>/', views.view_masscom_year3_second_semester, name='view_masscom_year3_second_semester'),
    path('upload_masscom_course6/', views.upload_masscom_course6, name='upload_masscom_course6'),

     # ***************************************
                 # YEAR 4 SEMESTER 1
    #*****************************************
    path('masscom_year4_first_semester/', views.masscom_year4_first_semester, name='masscom_year4_first_semester'),
    path('edit_masscom_year4_first_semester/<int:pk>/', views.edit_masscom_year4_first_semester, name='edit_masscom_year4_first_semester'),
    path('delete_masscom_year4_first_semester/<int:pk>/', views.delete_masscom_year4_first_semester, name='delete_masscom_year4_first_semester'), 
    path('view_masscom_year4_first_semester/<int:pk>/', views.view_masscom_year4_first_semester, name='view_masscom_year4_first_semester'),
    path('upload_masscom_course7/', views.upload_masscom_course7, name='upload_masscom_course7'),


     # ***************************************
                 # YEAR 4 SEMESTER 2
    #*****************************************
    path('masscom_year4_second_semester/', views.masscom_year4_second_semester, name='masscom_year4_second_semester'),
    path('edit_masscom_year4_second_semester/<int:pk>/', views.edit_masscom_year4_second_semester, name='edit_masscom_year4_second_semester'),
    path('delete_masscom_year4_second_semester/<int:pk>/', views.delete_masscom_year4_second_semester, name='delete_masscom_year4_second_semester'), 
    path('view_masscom_year4_second_semester/<int:pk>/', views.view_masscom_year4_second_semester, name='view_masscom_year4_second_semester'),
    path('upload_masscom_course8/', views.upload_masscom_course8, name='upload_masscom_course8'),
    
]
