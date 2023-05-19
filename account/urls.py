from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
<<<<<<< HEAD
    path("", views.index, name="index"),
    path("signUp", views.user_signup, name="signUp"),
    path("login", views.user_login, name="login")
=======
    path("", views.layout, name="layout"),
    path("signUp", views.signUp, name="signUp"),
    path("login", views.login, name="login")
>>>>>>> fd7d3e1cbe956fd24fa030075dd16838d57b7401
]