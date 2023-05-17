from django.urls import path
from . import views
urlpatterns = [
    path("", views.layout, name="layout"),
    path("signUp", views.signUp, name="signUp"),
    path("login", views.login, name="login")
]