from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm, CertificateForm

# Create your views here.
def index(request):
    """
    Default Accounts App Landing Page
    """
    return render(request, "account/authentication.html")

def user_signup(request):
    """
    This function is responsible for user registration
    """
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'account/signup.html', {'form' : form })

    if request.method == "POST":
        form = RegisterForm(request.POST)
        #Should Add Employeeand Employer Validation
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login (request, user)
            return redirect(request, 'base.html')
    return render(request, 'account/signup.html', {'form' : form })
        
def user_login(request):
    """
    This Function Logins in an authenticated User
    """
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("landing_page")
        else:
            return render(request, 'account/login.html')

def user_logout(request):
    """
    Function used to logout user
    """
    logout(request)
    messages.success(request, ("You were successfully Logged Out"))
    return redirect ("index.html")


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
