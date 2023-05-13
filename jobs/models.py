from django.db import models

# Create your models here.

"""
Models for the jobs app
 Table jobs
"""

class jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=35)
    job_type = models.CharField(max_length=10)
    job_location = models.CharField(max_length=35)
    description = models.CharField(max_length=4000)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    Date_posted = models.DateTimeField(auto_now_add=True)
   # employer_id = models.IntegerField() to be imported from account app


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


class applications(models.Model):
    """
    Model for jobseeker applications
    """
    application_id = models.AutoField(primary_key=True)
    #job_seeker_id = models.ForeignKey('account.jobseeker', on_delete=models.CASCADE)
    job_id = models.ForeignKey(jobs, on_delete=models.CASCADE)
    job_title = models.ForeignKey(jobs, on_delete=models.CASCADE)
    status = models.IntegerField(choices=((1, 'Pending'), (2, 'Accepted'), (3, 'Rejected'), (4, 'Done')))
    applicant_id = models.IntegerField()
    application_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'applications'
        verbose_name_plural = 'applications'

    def __str__(self):
        return self.status