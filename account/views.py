from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Your account page")

def signUp(request):
    return render(request, 'account/signup.html')
def login(request):
    return render(request, 'account/login.html')