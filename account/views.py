<<<<<<< HEAD
from django.contrib.auth import authenticate, login
=======

>>>>>>> fd7d3e1cbe956fd24fa030075dd16838d57b7401
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
<<<<<<< HEAD
def index(request):
    """
    This is the landing autentication Page 
    """
    return render(request, "authentication.html")
=======
def layout(request):
    return HttpResponse("This is the home page")
>>>>>>> fd7d3e1cbe956fd24fa030075dd16838d57b7401

def user_signup(request):
    """
    This function is responsible for user registration
    """
    return render(request, 'account/signup.html')
def user_login(request):
    """
    This Function Logins in an authenticated User
    """
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        #return redirect()
    else:
        return render(request, 'account/login.html')
    