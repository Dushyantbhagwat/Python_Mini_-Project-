from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

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


# class UserProfile(generic.TemplateView):
#     template_name = 'job_seeker/UserProfile.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         logged_in_user_id = self.kwargs.get('logged_in_user_id')  # Get the parameter from URL
#         context['logged_in_user_id'] = logged_in_user_id
#         # Add other necessary context data
#         return context





