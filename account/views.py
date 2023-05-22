from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

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
    return render(request, 'account/signup.html')
def user_login(request):
    """
    This Function is responsible for user login 
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
    return redirect ("landing_page")
