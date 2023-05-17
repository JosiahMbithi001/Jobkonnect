from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
    path("", views.layout, name="layout"),
    path("signUp", views.signUp, name="signUp"),
    path("login", views.login, name="login")
]