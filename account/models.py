
from django.db import models


class User(models.Model):
    """A model representing the users of JobKonnect website."""

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
        return self.username +" "+self.role


class Employer(models.Model):
    """A model representing an employer on JobKonnect website."""

    userid = models.AutoField(primary_key=True)
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
        return self.firstname+" "+self.lastname+" "+self.email


class Employee(models.Model):
    """A model representing an employee on JobKonnect website."""

    userid = models.AutoField(primary_key=True)
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
        return self.firstname+" "+self.lastname+" "+self.email
    
class Certificate(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date_of_issuance = models.DateField()
    certificate_file = models.FileField(upload_to='certificates/')

    class Meta:
        managed = True
        db_table = 'Certificate'
        verbose_name_plural = 'Certificates'
