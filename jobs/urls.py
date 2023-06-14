from django.urls import path, include
from .views import *

"""
URL configuration for jobs app
"""
urlpatterns = [
    path('', jobseeker_landing, name='employee_landing'),
    path('apply_job', ApplicationCreateView.as_view(), name='jobaplication'),
    path('<employee_name/applications', applicationhistory, name='aplicationhistory'),
    
    path('landing', employer_landing, name="employer_landing"),
    path('post_job', post_job, name='post_job'),
    path('search',search_job.as_view(), name='search_job'),
   
    ]