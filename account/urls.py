from django.urls import path,include
from . import views

urlpatterns = [
    path('student_home/', views.student_home, name='student_home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('login2/', views.login_view2, name='login2'),
    path('logout/', views.logout_view, name='logout'),
    
  
]