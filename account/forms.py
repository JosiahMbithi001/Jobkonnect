from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    """This Class is for Form Registration"""
    class Meta:
        model = User
        fields = ['username', 'email', 'password']