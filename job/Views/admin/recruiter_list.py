from django.shortcuts import render, redirect

from job.models import Recruiter


def recruiter_list(request):
    recruiters = Recruiter.objects.all()
    return render(request, 'admin/recruiter_list.html', {'recruiters': recruiters})
