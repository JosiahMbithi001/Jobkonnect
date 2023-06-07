from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Employer, Employee
from django.contrib.auth.models import User
import random 
from .forms import RegisterForm, CertificateForm, EmployeeForm, EmployerForm

# Create your views here.
def base(request):
    """
    This is the landing autentication Page 
    """
    return render(request, "account/authenticate.html")

def employer_sign_up(request):
    """Employers View for the SignUp Form"""
  
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        password = request.POST['password']
        location = request.POST['location']
        username = f'{firstname}{random.randint(1, 9999)}'

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=firstname,
                last_name=lastname,
                is_staff=True
            )

            employer = Employer(
                userid=user,
                firstname=firstname,
                lastname=lastname,
                phonenumber=phonenumber,
                email=email,
                password=password,
                location=location
            )
            employer.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect("/account/login")
        
    return render(request, 'account/employer.html')

def employee_sign_up(request):
    """Employee signup View"""

    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        password = request.POST['password']
        location = request.POST['location']
        profession = request.POST['profession']
        status = 'active'
        user_name = f'{firstname}{random.randint(1, 9999)}'
        if User.objects.filter(username=user_name).exists():
            messages.error(request, 'Username is already taken.')
        else:
            new_user = User.objects.create_user(
                username=user_name,
                password=password,
                email=email,
                first_name=firstname,
                last_name=lastname,
                is_staff=True
            )
        new_employee = Employee(
            user=new_user,
            firstname=firstname,
            lastname=lastname,
            phonenumber=phonenumber,
            email=email,
            password=password,
            location=location,
            profession=profession,
            status=status
        )
        new_employee.save()
        return redirect('/account/login')
    else:
        return render(request, 'account/employee.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, ("You were successfully Logged In"))
            if Employer.objects.filter(userid=request.user).exists():
                return redirect("/employer/landing")
            elif Employee.objects.filter(user=request.user).exists():
                return redirect("/employee/")
            else:
                return redirect("/account/login")
        else:
            messages.success(request, ("Error Logging In - Please Try Again..."))
            return redirect("/account/login")
    else:
        return render(request, 'account/login.html')

def user_logout(request):
    """
    Function used to logout user
    """
    logout(request)
    messages.success(request, ("You were successfully Logged Out"))
    return redirect ("/")


def upload_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.save()
            return redirect('certificate_list')
    else:
        form = CertificateForm()
    return render(request, 'upload_certificate.html', {'form': form})