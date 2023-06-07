from django.shortcuts import render, redirect
from .models import Job, Application
from account.models import Employee, Employer
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
        job_title = request.POST.get('job_title')
        job_type = request.POST.get('job_type')
        job_status = 1
        job_location = request.POST.get('job_location')
        description = request.POST.get('description')
        salary = request.POST.get('salary')
        requirements = request.POST.get('requirements')

        # Get the employer ID of the currently signed-in user
        if Employee.objects.filter(userid=request.user):
            return redirect('/employee')
        elif Employer.objects.filter(userid=request.user):
            employer = Employer.objects.get(userid=request.user)
            this_job = Job.objects.create(
                job_title=job_title,
                job_type=job_type,
                job_status=job_status,
                job_location=job_location,
                description=description,
                salary=salary,
                requiments=requirements,
                user_id=employer
            )
            # Redirect to the employer dashboard
            return redirect('/employer/landing')
    else:
        return render(request, 'post.html')
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
        return redirect('jobs/post.html')
    else:
        # Render the form for applying to a job
        return render(request, 'jobs/post.html')

def jobseeker_landing(request):
    """
    This view will handle the jobseeker landing page
    Check on how to filter based on the status, professionalism, location
    """
    #get all jobs
    jobs = Job.objects.all()
    return render(request, 'jobs/employee_landing.html', {'jobs': jobs})
@login_required
def employer_landing(request):
    """
    This view will handle the employer landing page
    Not sure if it will work
    add a logic to enable employer see the applicant account
    """
    employer = Employer.objects.get(userid=request.user)

    job_posted = Job.objects.filter(user_id=employer)
    #job_posted = Job.objects.get(user_id=request.Employer)
    if job_posted:
        # applications = Application.objects.filter(job_id__in = job_posted)
        return render(request, 'jobs/employer_landing.html', {'jobs': job_posted})
    else:
        employees = Employee.objects.filter(location=Employer.location)
        return render(request, 'jobs/employer_landing.html', {'employees': employees})

@login_required
def applicationhistory(request):
    """
    This function handles the jobseeker application history
    check on filtering b employee id
    """
    employee_id = Employee.objects.get(user=request.user)
    all_aplications = Application.objects.filter(employee_id=employee_id)

    return render (request, 'jobs/', {'all_aplications': all_aplications})

