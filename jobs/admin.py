from django.contrib import admin

# Register your models here.
from .models import jobs, applications

admin.site.register(jobs)
admin.site.register(applications)