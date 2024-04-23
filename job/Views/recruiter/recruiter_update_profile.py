from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from job.models import JobSeeker, Recruiter
from django.views import View


from django.contrib import messages
from django.shortcuts import redirect


class UpdateProfile(View):
    template_name = 'recruiter/RUpdateProfile.html'

    def get(self, request, *args, **kwargs):
        logged_in_user_id = request.session.get('logged_in_user_id')

        if logged_in_user_id:
            try:
                recruiter = Recruiter.objects.get(id=logged_in_user_id)
                return render(request, self.template_name, {'recruiter': recruiter})
            except Recruiter.DoesNotExist:
                return HttpResponse("Job Seeker does not exist.")
        else:
            return HttpResponse("Logged in user ID not found in session.")

    def post(self, request):
        try:
            activity = request.POST.get('activity')
            skills = request.POST.get('skills')
            company = request.POST.get('company')
            photo = request.FILES.get('photo')  # Use get() to avoid KeyError

            activity = activity.title()

            recruiter = Recruiter.objects.get(id=request.session.get('logged_in_user_id'))
            recruiter.past_activity = activity
            recruiter.skills = skills
            recruiter.company_name = company
            if photo:  # Check if photo is uploaded
                print("yes")
                recruiter.image = photo
            recruiter.save()

            messages.success(request, "Profile Updated Successfully")
            return redirect('r_profile')  # Redirect to the profile page
        except JobSeeker.DoesNotExist:
            # Handle the case where JobSeeker does not exist
            return HttpResponse("Job Seeker does not exist.")
        except Exception as e:
            # Handle other exceptions
            messages.error(request, f"An error occurred: {str(e)}")
            logged_in_user_id = request.session.get('logged_in_user_id')
            recruiter = Recruiter.objects.get(id=logged_in_user_id)
            return render(request, self.template_name, {'recruiter': recruiter})

