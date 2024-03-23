from django.http import HttpResponse
from django.shortcuts import render, redirect

from job.models import Recruiter


def recruiter_profile(request):
    # Retrieve logged_in_user_id from session
    logged_in_user_id = request.session.get('logged_in_user_id')

    if logged_in_user_id:
        try:
            # Assuming you have a Recruiter model
            recruiter = Recruiter.objects.get(id=logged_in_user_id)
            return render(request, 'recruiter/RecruiterProfile.html', {'recruiter': recruiter})
        except Recruiter.DoesNotExist:
            # Handle the case where the recruiter does not exist
            return HttpResponse("Recruiter does not exist.")
    else:
        # Handle the case where logged_in_user_id is not found in session
        return HttpResponse("Logged in user ID not found in session.")


