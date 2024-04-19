from django.contrib import messages
from django.shortcuts import render, redirect

from job.models import JobSeeker
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.core.mail import send_mail, EmailMessage


def registered_seeker_list(request):
    job_seekers = JobSeeker.objects.all()
    # paginator = Paginator(job_seekers, 5)

    # page_number = request.GET.get('page')
    # page_object = paginator.get_page(page_number)
    return render(request, 'admin/job_seeker_list.html', {'job_seekers': job_seekers})


def delete_job_seeker(request, user_id):
    # Retrieve the JobSeeker object
    job_seeker = JobSeeker.objects.get(id=user_id)

    # Delete the associated User object
    user = job_seeker.user
    user.delete()

    # Delete the JobSeeker object
    job_seeker.delete()

    return render(request, 'admin/job_seeker_list.html')



