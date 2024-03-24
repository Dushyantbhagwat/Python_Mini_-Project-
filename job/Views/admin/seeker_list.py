from django.contrib import messages
from django.shortcuts import render, redirect

from job.models import JobSeeker


def registered_seeker_list(request):
    job_seekers = JobSeeker.objects.all()
    return render(request, 'admin/job_seeker_list.html', {'job_seekers': job_seekers})


def delete_job_seeker(request, job_seeker_id):
    return redirect('')  # Redirect to an error page or another URL
