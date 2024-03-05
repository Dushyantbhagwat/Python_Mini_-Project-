from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.views import generic, View
from .models import JobSeeker
from .utils import *
from django.contrib import messages
from django.core.exceptions import ValidationError


# Create your Views here.

class LandingPage(generic.TemplateView):
    template_name = 'landing_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve data from the database
        options = JobSeeker.objects.values_list('location', flat=True).distinct()
        context['options'] = options
        return context


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = JobSeeker.objects.filter(email_id=email).first()

            if user and check_password(password, user.password):
                messages.success(request, "successfull")
                request.session['logged_in_user_id'] = user.id
                print(f"JobSeeker details - Name: {user.full_name}, Email: {user.email_id}, Mobile: {user.mobile_no}, "
                      f"Location: {user.location}")
                return redirect('u1')

            print(user.full_name)

        except ValidationError as e:
            messages.warning(request, f"Fail: {str(e)}")

        return render(request, self.template_name)


def u1(request):
    # Retrieve the ID of the logged-in user from the session
    logged_in_user_id = request.session.get('logged_in_user_id')
    if logged_in_user_id:
        # User is logged in, retrieve details based on the ID
        try:
            job_seeker = JobSeeker.objects.get(id=logged_in_user_id)
            # Do something with job_seeker object
            return render(request, 'u1.html', {'job_seeker': job_seeker})
        except JobSeeker.DoesNotExist:
            # Handle case where no JobSeeker instance is found for the logged-in user
            return render(request, 'dashboard.html', {'error': 'JobSeeker instance not found'})
    else:
        # User is not logged in, handle accordingly
        return redirect('login')


def job(request):
    return render(request, 'j1.html')


