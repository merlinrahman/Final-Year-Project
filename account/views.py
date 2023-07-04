
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from account.forms import  UserRegistrationForm,UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# ***********************************************************************AUTHENTICATION*********************************************************
# REGISTRATION
@login_required(login_url='login')
def register(request):
    context={}
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student registered successfully! ")
            return redirect('register')
        context['register_form'] = form
    else:
        form = UserRegistrationForm()
        context['register_form'] = form
    return render(request, 'result/register.html', context)



# LOGIN
def login_view(request):
    context={}
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request,email=email,password=password)
            if user is not None:
                login(request, user)
                return redirect("admin1")
        else:
            context['login_form'] = form
    else:
        form=UserLoginForm()
        context['login_form'] = form
    return render(request, "result/login_register.html", context)


# LOGOUT

def logout_view(request):
    logout(request)
    return redirect('login_register')



# STUDENT-HOME
@login_required(login_url='login')
def student_home(request):
    return render(request, 'result/student_home.html', {})







