from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from job.models import JobSeeker
from django.views import View


from django.contrib import messages
from django.shortcuts import redirect


class UpdateProfileView(View):
    template_name = 'job_seeker/u_update_profile.html'

    def get(self, request, *args, **kwargs):
        logged_in_user_id = request.session.get('logged_in_user_id')

        if logged_in_user_id:
            try:
                job_seeker = JobSeeker.objects.get(id=logged_in_user_id)
                return render(request, self.template_name, {'job_seeker': job_seeker})
            except JobSeeker.DoesNotExist:
                return HttpResponse("Job Seeker does not exist.")
        else:
            return HttpResponse("Logged in user ID not found in session.")

    def post(self, request):
        try:
            name = request.POST.get('name')
            gender = request.POST.get('gender')
            mobile = request.POST.get('phone')
            email = request.POST.get('email')
            photo = request.FILES.get('photo')  # Use get() to avoid KeyError
            address = request.POST.get('address')
            resume = request.FILES.get('resume')

            name = name.title()

            job_seeker = JobSeeker.objects.get(id=request.session.get('logged_in_user_id'))
            job_seeker.full_name = name
            job_seeker.gender = gender
            job_seeker.mobile_no = mobile
            job_seeker.email_id = email
            if photo:  # Check if photo is uploaded
                job_seeker.image = photo
            job_seeker.address = address
            job_seeker.resume = resume
            job_seeker.save()

            messages.success(request, "Profile Updated Successfully")
            return redirect('u_profile')  # Redirect to the profile page
        except JobSeeker.DoesNotExist:
            # Handle the case where JobSeeker does not exist
            return HttpResponse("Job Seeker does not exist.")
        except Exception as e:
            # Handle other exceptions
            messages.error(request, f"An error occurred: {str(e)}")
            logged_in_user_id = request.session.get('logged_in_user_id')
            job_seeker = JobSeeker.objects.get(id=logged_in_user_id)
            return render(request, self.template_name, {'job_seeker': job_seeker})

