from django.urls import path
from . import views



urlpatterns = [

                  # LOGIN-REGISTER PAGE
    #***************************************
    path('login_register/', views.login_register, name='login_register'),

    # ***************************************
                 # HOME PAGE
    #*****************************************
    path('', views.admin2, name='admin2'),

       # ***************************************
                 # ADMIN1
    # *****************************************
    path('admin2/', views.admin2, name='admin2'),

    #***************ADMIN LOGIN***************8
    path('admin-redirect/', views.admin_redirect, name='admin_redirect'),
]