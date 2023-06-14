from django.shortcuts import render, redirect
from .models import Job, Application
from account.models import Employee, Employer
from django.views.generic import View, ListView
from django.http import HttpResponse, request
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

        if Employee.objects.filter(user=request.user).exists():
            return redirect('/employee/')
        elif Employer.objects.filter(userid=request.user).exists():
            user = Employer.objects.get(userid=request.user)
            this_job = Job.objects.create(
                job_title=job_title,
                job_type=job_type,
                job_status=job_status,
                job_location=job_location,
                description=description,
                salary=salary,
                requiments=requirements,
                user_id=user
            )
            return redirect('/employer/landing')
        else:
            return redirect('/employee/')
    else:
        return render(request, 'post.html')
    


@method_decorator(login_required, name='dispatch')
class ApplicationCreateView(View):
    template_name = 'jobs/employee_landing.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        employee = Employee.objects.get(user_id=request.user)
        job_id = request.POST.get('jobid')
        job = Job.objects.get(job_id = job_id)
        userid = employee
        status = 'pending'  # Set default status to 'Pending'
        proposal = request.POST.get('proposal')
        cv = request.FILES.get('cv')
        estimated_salary = request.POST.get('estimated_salary')

        application = Application.objects.create(
            job_id=job,
            status=status,
            proposal=proposal,
            userid=userid,
            cv=cv,
            estimated_salary=estimated_salary
        )
        apply = application
        
        # Redirect to jobseeker dashboard or another appropriate page
        if apply:
            return redirect('/employee/')
        else:
            return render(request, 'jobs/employee_landing.html')

def jobseeker_landing(request):
    """
    This view will handle the jobseeker landing page
    Check on how to filter based on the status, professionalism, location
    """
    queryset = Job.objects.all()
    context_object_name = 'jobs'
    paginator = Paginator(queryset, 3)
    page = request.GET.get('page')
    template_name = 'jobs/employee_landing.html'
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    return render(request, template_name, {'jobs': queryset, 'page': page, 'context_object_name': context_object_name})




class search_job(ListView):
    """
    This view will handle the jobseeker landing page
    """
    template_name = 'jobs/employee_landing.html'
    paginate_by = 2
    context_object_name = 'jobs'

    def get_queryset(self):
        location = self.request.POST.get('location')
        job_type = self.request.POST.get('job_type')
        if location and job_type:
            queryset = Job.objects.filter(job_location=location, job_type=job_type)
        elif location:
            queryset = Job.objects.filter(job_location=location)
        elif job_type:
            queryset = Job.objects.filter(job_type=job_type)
        else:
            queryset = Job.objects.all()
        return queryset
@login_required
def employer_landing(request):
    """
    This view will handle the employer landing page
    Not sure if it will work
    add a logic to enable employer see the applicant account
    """
    employer = Employer.objects.get(userid=request.user)

    job_posted = Job.objects.filter(user_id=employer)
    if job_posted:
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

