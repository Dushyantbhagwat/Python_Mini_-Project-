from django.shortcuts import render, redirect

from job.models import Recruiter


def recruiter_list(request):
    recruiters = Recruiter.objects.filter(status='request pending')
    return render(request, 'admin/recruiter_list.html', {'recruiters': recruiters})


def accepted_recruiter_list(request):
    recruiters = Recruiter.objects.filter(status='Accepted')
    return render(request, 'admin/recruiter_list.html', {'recruiters': recruiters})


def rejected_recruiter_list(request):
    recruiters = Recruiter.objects.filter(status='Rejected')
    return render(request, 'admin/recruiter_list.html', {'recruiters': recruiters})
