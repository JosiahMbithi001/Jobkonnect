from django.db import models
import datetime
# Create your models here.

"""
Models for the jobs app
 Table jobs
"""

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50)
    job_status = models.IntegerField(choices=((1, 'Active'), (2, 'Inactive')))
    job_location = models.CharField(max_length=500)
    description = models.CharField(max_length=4000)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    Date_posted = models.DateTimeField(auto_now_add=True)
   # employer = oneToManyField(employer, on_delete=models.CASCADE) to be imported from account app


    class Meta:
        """
        Meta class for jobs model
        setted managed to True to create a table in the database
        using django orm
        """
        managed = True
        db_table = 'jobs'
        verbose_name_plural = 'jobs'

    def __str__(self):
        return self.job_title


class Application(models.Model):
    """
    Model for jobseeker applications
    """
    application_id = models.AutoField(primary_key=True)
<<<<<<< HEAD
    job_seeker_id = models.ForeignKey('account.jobseeker', on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
=======
    #job_seeker_id = models.ForeignKey('account.jobseeker', on_delete=models.CASCADE)
    job_id = models.ForeignKey(jobs, on_delete=models.CASCADE)
    #job_title = models.ForeignKey(jobs, on_delete=models.CASCADE)
>>>>>>> 19f35fee6084b7de9e3e5327b4da6abed7b40676
    status = models.IntegerField(choices=((1, 'Pending'), (2, 'Accepted'), (3, 'Rejected'), (4, 'Done')))
    application_date = models.DateTimeField(auto_now_add=True)
    proposal = models.TextField(max_length=4000)
    # cv = to be uploaded
    estimated_salary = models.IntegerField(max_length=40000)

    class Meta:
        managed = True
        db_table = 'applications'
        verbose_name_plural = 'applications'

    def __str__(self):
        return self. self.job_id.job_title + self.status