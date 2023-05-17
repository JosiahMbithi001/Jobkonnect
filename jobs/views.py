from django.shortcuts import render, redirect
from .models import Job, Application
from django.http import HttpResponse, request

"""
The jobs app views will handle the following:
Employer posts a job and it is saved in the database
    -This will be handled by post
Jobseeker can see available jobs based on their location:
    -This will be handled by a get request on jobseeker landing page
Jobseeker can apply for a job. 
    -This will be handled by a post request which will be saved on db
        aplication table and a notification will be trigerred to the 
        employer to notify him/her about the aplication and then to jobseeker
Employer can see the aplications made to his job post by jobseekers
jobseeker can see the aplication status and history
"""

# Create your views here.
def post_job(request):
    """
    This view will handle the posting of jobs by employers
    """
    if request.method == 'POST':
        job_title = request.POST['job_title']
        job_type = request.POST['job_type']
        job_status = request.POST['job_status']
        job_location = request.POST['job_location']
        description = request.POST['description']
        min_salary = request.POST['min_salary']
        max_salary = request.POST['max_salary']
        #employer_id = request.POST['employer_id']
        this_job = Job(job_title=job_title, job_type=job_type, job_status=job_status, job_location=job_location, description=description, min_salary=min_salary, max_salary=max_salary)
        this_job.save()
        #redirect to employer dashboard
        return redirect('/employer/')
    else:
        # check a way to hundle errors, and then if it incorrect
        #  info provided return the user to the same file
        return render(request, 'jobs/')

def  apply_job(request):
    """
    This view will handle the application of jobs by jobseekers
    """
    if request.method == 'POST':
        job_id = request.POST['job_id']
        job_title = request.POST['job_title']

        #job_seeker_id = request.POST['job_seeker_id']
        apply_job = Application(job_id=job_id, job_title=job_title)
        apply_job.save()
        #redirect to jobseeker dashboard
        return redirect('/jobseeker/')
    else:
        return render(request, 'jobs/')

def jobseeker_landing(request):
    """
    This view will handle the jobseeker landing page
    Check on how to filter based on the status, professionalism, location
    """
    #get all jobs
    all_jobs = Job.objects.all()
    return render(request, 'jobseeker/index.htm', {'all_jobs': all_jobs})


def employer_landing(request):
    """
    This view will handle the employer landing page
    Show available jobseekers if no job posted
    Show aplications made to his/her job post
    """

def aplicationhistory(request):
    """
    This function handles the jobseeker application history
    check on filtering b employee id
    """
    all_aplications = Application.objects.all()

    return render (request, 'jobs/', {'all_aplications': all_aplications})

