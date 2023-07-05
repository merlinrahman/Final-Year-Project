from django.urls import path, include
from . import views


urlpatterns = [

    # ***************************************
                 # HOME PAGE
    #*****************************************
    path('', views.index, name='index'),

    # ***************************************
                 # ABOUT PAGE
    #*****************************************
    path('about/', views.about, name='about'),

               # CONTACT PAGE
    #*****************************************
    path('contact/', views.contact, name='contact'),

              # LOGIN-REGISTER PAGE
    #***************************************
    path('login_register/', views.login_register, name='login_register'),



    # CUSL HOME PAGE
    #***************************************
    path('cusl_home/', views.cusl_home, name='cusl_home'),

  

    # CUSL HOME PAGE
    #***************************************
    path('njala_home/', views.njala_home, name='njala_home'),

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
                 # MODULES/COURSES
    #*****************************************
    path('course/', views.course, name='course'),
    path('edit_course/<int:pk>/', views.edit_course, name='edit_course'),
    path('delete_course/<int:pk>/', views.delete_course, name='delete_course'), 
    path('view_course/<int:pk>/', views.view_course, name='view_course'),
    path('upload_course/', views.upload_course, name='upload_course'),




    # ***************************************
                 #  STUDENTS
    #*****************************************
    path('student/', views.student, name='student'),
    path('edit_student/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'), 
    path('view_student/<int:pk>/', views.view_student, name='view_student'),
    # path('upload_level/', views.upload_level, name='upload_level'),




    # ***************************************
                 #  STUDENTS RESULTS
    #*****************************************
    path('result/', views.result, name='result'),
    path('edit_result/<int:pk>/', views.edit_result, name='edit_result'),
    path('delete_result/<int:pk>/', views.delete_result, name='delete_result'), 
    path('view_result/<int:pk>/', views.view_result, name='view_result'),
    # path('upload_level/', views.upload_level, name='upload_level'),






     # ***************************************
                 #  Searching for result
    #*****************************************
    path('search_result/', views.search_result, name='search_result'),
    path('view_student_result/<str:email>/<str:id_number>/', views.view_student_result, name='view_student_result'),
    
]
