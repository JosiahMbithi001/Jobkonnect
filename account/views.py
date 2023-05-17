
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def layout(request):
    return HttpResponse("This is the home page")

def signUp(request):
    return render(request, 'account/signup.html')
def login(request):
    return render(request, 'account/login.html')