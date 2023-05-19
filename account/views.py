
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CertificateForm
from django.http import HttpResponse

def index(request):
    """
    This is the landing autentication Page 
    """
    return render(request, "authentication.html")
def user_signup(request):
    """
    This function is responsible for user registration
    """
    return render(request, 'account/signup.html')
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
            #return redirect()
    else:
        return render(request, 'account/login.html')


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