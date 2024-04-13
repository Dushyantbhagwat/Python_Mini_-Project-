from django.contrib import admin
from .models import JobSeeker, Recruiter, Job, Application
# Register your models here.

admin.site.register(JobSeeker)
admin.site.register(Recruiter)
admin.site.register(Job)
