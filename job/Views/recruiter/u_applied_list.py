from django.shortcuts import render

from job.models import Application


def applied_seeker(request, app_id):
    return render(request, 'recruiter/ApplicationList.html')
