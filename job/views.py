from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.views import generic, View
from .models import JobSeeker, Recruiter
from .utils import *
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import JsonResponse
import random

# Create your Views here.


class LandingPage(generic.TemplateView):
    template_name = 'landing_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve data from the database
        options = JobSeeker.objects.order_by('city').values_list('city', flat=True).distinct()
        print(f"{options}")
        context['options'] = options
        print(context)
        return context


# class LoginView(View):
#     template_name = 'Login.html'
#
#     def get(self, request):
#         return render(request, self.template_name)
#
#     def post(self, request):
#         email = request.POST.get('email')
#         password = request.POST.get('pwd')
#
#         user = authenticate(username=email, password=password)
#
#         if user:
#             try:
#                 # check if the user is in the JobSeeker table
#                 user1 = JobSeeker.objects.get(user=user)
#
#                 if user1.type == 'seeker':
#                     request.session['logged_in_user_id'] = user1.id
#                     print(f"JobSeeker details - Name: {user1.full_name}, Email: {user1.email_id},"
#                           f" Mobile: {user1.mobile_no}")
#                     return redirect('u1')
#
#                 # check if the user is in the Recruiter table
#                 user2 = Recruiter.objects.get(user=user)
#
#                 if user2.type == 'recruiter':
#                     request.session['logged_in_user_id'] = user2.id
#                     print(f"{user2.full_name}")
#                     return redirect('login')
#
#             except ValidationError as e:
#                 messages.warning(request, f"Fail: {str(e)}")
#
#         return render(request, self.template_name)

class LoginView(View):
    template_name = 'Login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('pwd')

        print("Received email:", email)  # Debug statement
        print("Received password:", password)  # Debug statement

        user = authenticate(username=email, password=password)

        if user:
            print("User authenticated successfully.")  # Debug statement

            try:
                # Check if the user is a JobSeeker
                job_seeker = JobSeeker.objects.get(user=user)
                if job_seeker.type == 'seeker':
                    request.session['logged_in_user_id'] = job_seeker.id
                    print(f"JobSeeker details - Name: {job_seeker.full_name}, Email: {job_seeker.email_id},"
                          f" Mobile: {job_seeker.mobile_no}")
                    return render(request, 'job_seeker/u_landing_page.html', {'job_seeker': job_seeker})

            except JobSeeker.DoesNotExist:
                pass  # No JobSeeker found for this user

            try:
                # Check if the user is a Recruiter
                recruiter = Recruiter.objects.get(user=user)
                if recruiter.type == 'recruiter':
                    request.session['logged_in_user_id'] = recruiter.id
                    print(f"{recruiter.full_name}")
                    # return ('landing_page')  # Redirect to recruiter dashboard
                    return render(request, 'recruiter/RLandingPage.html', {'recruiter': recruiter})

            except Recruiter.DoesNotExist:
                pass  # No Recruiter found for this user

            messages.warning(request, "You are not authorized to access this page.")

        else:
            print("Authentication failed.")  # Debug statement
            messages.error(request, "Invalid email or password.")

        return render(request, self.template_name)


# def u1(request):
#     # Retrieve the ID of the logged-in user from the session
#     logged_in_user_id = request.session.get('logged_in_user_id')
#     if logged_in_user_id:
#         # User is logged in, retrieve details based on the ID
#         try:
#             job_seeker = JobSeeker.objects.get(id=logged_in_user_id)
#             # Do something with job_seeker object
#             return render(request, 'u1.html', {'job_seeker': job_seeker})
#         except JobSeeker.DoesNotExist:
#             # Handle case where no JobSeeker instance is found for the logged-in user
#             return render(request, 'dashboard.html', {'error': 'JobSeeker instance not found'})
#     else:
#         # User is not logged in, handle accordingly
#         return redirect('login')


def job(request):
    return render(request, 'j1.html')


def logout(request):
    del request.session['logged_in_user_id']
    messages.success(request, 'Logged out successfully')
    return render(request, 'Login.html')
