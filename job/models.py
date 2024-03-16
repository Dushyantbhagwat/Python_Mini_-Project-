from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Recruiter(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    full_name = models.CharField(max_length=200, null=False)
    email_id = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=200, null=False)
    company_name = models.CharField(max_length=200, null=False)
    mobile = models.CharField(max_length=10, null=False)
    website = models.CharField(max_length=200, blank=True, null=True)
    past_activity = models.CharField(max_length=200, blank=True, null=True)
    skills = models.CharField(max_length=200, blank=True, null=True)
    company_details = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True, default='request pending')
    type = models.CharField(max_length=45, blank=True, null=True, default='recruiter')
    image = models.ImageField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class JobSeeker(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    full_name = models.CharField(max_length=200, null=False)
    email_id = models.CharField(unique=True, max_length=200, null=False)
    password = models.CharField(max_length=200, null=False)
    mobile_no = models.CharField(max_length=10, null=False)
    city = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=200, null=False)
    resume = models.FileField(upload_to='', max_length=100, blank=True, null=True)
    type = models.CharField(max_length=45, null=True, default='seeker')
    image = models.ImageField(upload_to='user', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Job(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=45, null=False)
    salary = models.CharField(max_length=45, null=True, default='Not Disclosed')
    skills = models.CharField(max_length=45, null=False)
    job_type = models.CharField(max_length=45, null=False)
    location = models.CharField(max_length=45, null=False)
    description = models.CharField(max_length=45, null=False)
    start_date = models.CharField(max_length=45, null=False)
    deadline = models.CharField(max_length=45, null=False)
    recruiter = models.ForeignKey('Recruiter', models.CASCADE)


class Application(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey('JobSeeker', models.CASCADE)
    job = models.ForeignKey('Job', models.CASCADE)


