from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views
from .views import upload_certificate

app_name = "account"
urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.user_signup, name="signup"),
    path("signup/employer", views.employer_sign_up, name="signupemployer"),
    path("signup/employee", views.employee_sign_up, name="signupemployee"),
    path("login/", views.user_login, name="login")
]
    # #path("", views.layout, name="layout"),
    # path("signUp", views.signUp, name="signUp"),
    # #path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    # #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # #path("login", views.login, name="login"),
    # path('upload-certificate', views.upload_certificate, name='upload_certificate')
