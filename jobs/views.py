from django.shortcuts import render, redirect
from .models import Job, Application
from account.models import Employee, Employer, User
from django.http import HttpResponse, request
from django.contrib.auth.decorators import login_required

"""
The jobs app views will handle the following:
Employer posts a job and it is saved in the database
    -This will be handled by  request
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
@login_required
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
        #employer_id = request.POST.get['employer_id']
        this_job = Job(
            job_title=job_title,
            job_type=job_type,
            job_status=job_status,
            job_location=job_location,
            description=description,
            min_salary=min_salary,
            max_salary=max_salary,
            #employer_id=employer_id
            )
        this_job.save()
        #redirect to employer dashboard
        return redirect('/employer/')
    else:
        return render(request, 'jobs/')
@login_required
def apply_job(request):
    if request.method == 'POST':
        job_id = request.POST('job_id')
        status = 1  # Set default status to 'Pending'
        proposal = request.POST('proposal')
        cv = request.FILES.get('cv')
        estimated_salary = request.POST('estimated_salary')

        application = Application(
            job_id=Job.objects.get(job_id=job_id),
            status=status,
            proposal=proposal,
            cv=cv,
            estimated_salary=estimated_salary
        )

        application.objects.create()
        
        # Redirect to jobseeker dashboard or another appropriate page
        return redirect('/jobseeker/')
    else:
        # Render the form for applying to a job
        return render(request, 'jobs/apply_job.html')
@login_required
def jobseeker_landing(request):
    """
    This view will handle the jobseeker landing page
    Check on how to filter based on the status, professionalism, location
    """
    #get all jobs
    all_jobs = Job.objects.all()
    return render(request, 'jobs/test.html', {'all_jobs': all_jobs})

@login_required
def employer_landing(request):
    """
    This view will handle the employer landing page
    Not sure if it will work
    add a logic to enable employer see the applicant account
    """
    job_posted = Job.objects.filter(user_id=request.user)
    if job_posted:
        applications = Application.objects.filter(job_id__in = job_posted)
        return render(request, 'employer/landingpage', {'application': applications})
    else:
        employees = Employee.objects.filter(location=Employer.location)
        return render(request, 'employer/landingpage', {'employees': employees})

@login_required
def aplicationhistory(request):
    """
    This function handles the jobseeker application history
    check on filtering b employee id
    """
    all_aplications = Application.objects.filter(user_id = User.userid)

    return render (request, 'jobs/', {'all_aplications': all_aplications})

