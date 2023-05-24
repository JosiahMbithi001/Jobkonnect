
from django.db import models
from django import forms


class User(models.Model):
    """A model representing the users of JobKonnect website."""
    REQUIRED_FIELDS = ['username', 'email', 'password']
    # def __init__(self, username, email, password):
    #     self.username = username
    #     self.email = email
    #     self.password = password

    ROLES = (
        ('employer', 'Employer'),
        ('employee', 'Employee'),
    )

    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=ROLES)

    class Meta:
        managed = True
        db_table = 'user'
        verbose_name_plural = "Users"
    
    def __str__(self):
        return str(self.userid)


class Employer(models.Model):
    """A model representing an employer on JobKonnect website."""

    employerid = models.AutoField(primary_key=True)
    userid =models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)
    location = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'employer'
        verbose_name_plural = "Employers"

    def __str__(self):
        return self.userid.username+" "+self.email


class Employee(models.Model):
    """A model representing an employee on JobKonnect website."""

    employeeid = models.AutoField(primary_key=True)
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phonenumber = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    status = models.CharField(max_length=15)

    class Meta:
        managed = True
        db_table = 'employee'
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.userid.username
    
class Certificate(models.Model):
    """This is an Employees Certificate"""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date_of_issuance = models.DateField()
    certificate_file = models.FileField(upload_to='certificates/')

    class Meta:
        managed = True
        db_table = 'Certificate'
        verbose_name_plural = 'Certificates'
