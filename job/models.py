from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Recruiter(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    full_name = models.CharField(max_length=200, null=False)
    email_id = models.CharField(max_length=200, null=False)
    company_name = models.CharField(max_length=200, null=False)
    mobile = models.CharField(max_length=10, null=False)
    website = models.CharField(max_length=200, blank=True, null=True)
    past_activity = models.CharField(max_length=200, blank=True, null=True)
    skills = models.CharField(max_length=200, blank=True, null=True)
    company_details = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True, default='request pending')
    type = models.CharField(max_length=45, blank=True, null=True, default='recruiter')
    image = models.ImageField(upload_to='recruiter', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class JobSeeker(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    full_name = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=10, blank=True, null=True)
    email_id = models.CharField(unique=True, max_length=200, null=False)
    mobile_no = models.CharField(max_length=10, null=False)
    city = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=200, null=False)
    resume = models.FileField(upload_to='user_resume', max_length=100, blank=True, null=True, default='not uploaded')
    type = models.CharField(max_length=45, null=True, default='seeker')
    image = models.ImageField(upload_to='user', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Job(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=45, null=False)
    description = models.CharField(max_length=45, null=False)
    city = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=45, null=False)
    start_date = models.CharField(max_length=45, null=False)
    deadline = models.CharField(max_length=45, null=False)
    minimum_salary = models.CharField(max_length=45, null=False, default='Not Disclosed')
    job_type = models.CharField(max_length=45, null=False)
    experience = models.CharField(max_length=50, null=False, default='not provided')
    skills = models.CharField(max_length=45, blank=True, null=False)
    recruiter = models.ForeignKey('Recruiter', models.CASCADE)
    rate = models.CharField(max_length=10, null=False)

    # def __str__(self):
    #     return f"{self.title} - {self.recruiter}"  # Modify this according to your fields


class Application(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey('JobSeeker', models.CASCADE)
    job = models.ForeignKey('Job', models.CASCADE)
    status = models.CharField(max_length=20, default='Pending')
    reason = models.CharField(max_length=200, default='Not Provided')


