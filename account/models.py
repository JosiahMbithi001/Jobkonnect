
from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name
    def employer(self):
        pass
    def employee(self):
        pass
