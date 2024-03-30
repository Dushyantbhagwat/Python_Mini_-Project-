from django.shortcuts import render

from job.models import Job, Application


def c_list(request):
    apps = Application.objects.all()
    return render(request, 'recruiter/ApplicationList.html', {'apps': apps})

