from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic, View

from job.models import JobSeeker


def seeker_profile(request):
    # Retrieve logged_in_user_id from session
    logged_in_user_id = request.session.get('logged_in_user_id')

    if logged_in_user_id:
        try:
            # Assuming you have a Recruiter model
            job_seeker = JobSeeker.objects.get(id=logged_in_user_id)
            return render(request, 'job_seeker/UserProfile.html', {'job_seeker': job_seeker})
        except JobSeeker.DoesNotExist:
            # Handle the case where the recruiter does not exist
            return HttpResponse("Recruiter does not exist.")
    else:
        # Handle the case where logged_in_user_id is not found in session
        return HttpResponse("Logged in user ID not found in session.")



