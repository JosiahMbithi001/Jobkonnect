from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Certificate, Employer, Employee


class EmployerForm(forms.ModelForm):
    """
    This is Employers Form
    """
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     #Loops and sets the required fields to True
    #     for field in self.fields.items():
    #         field.required = True
    
    class Meta:
        """
        Employers MetaData
        """
        model = Employer
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    """
    This is the Form Employees will Fill
    """
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     #Loops Through All Employee Fields and sets required to True
    #     for field in self.fields.items():
    #         field.required = True

    class Meta:
        """
        Employees MetaData
        """
        model = Employee
        fields = '__all__'

class RegisterForm(UserCreationForm):
    """This Class is for Form Registration"""
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CertificateForm(forms.ModelForm):
    """Where Users will display their Certificates"""

    class Meta:
        """Certificates Metadata"""
        model = Certificate
        fields = '__all__'
