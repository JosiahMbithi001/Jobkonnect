from django.urls import path, include
from .views import *

"""
URL configuration for jobs app
"""
urlpatterns = [
    path('employee/', jobseeker_landing, name='employee_landing'),
    path('employee/apply_job/<job_title>', apply_job, name='jobaplication'),
    path('employee/<employee_name/aplications', aplicationhistory, name='aplicationhistory'),
    
    path('employer/', employer_landing, name="employer_landing"),
    path('employer/post_job', post_job, name='post_job')
]