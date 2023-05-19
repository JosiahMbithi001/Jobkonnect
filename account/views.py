from django.contrib.auth import authenticate, login

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is the home page")

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
    