import re

from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import generic, View
from job.models import JobSeeker
from job.utils import *
from django.contrib import messages
from django.core.exceptions import ValidationError


class UserSignupView(View):
    template_name = 'signup.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:

            # Get form data from POST request
            name = request.POST.get('name')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            password = request.POST.get('password')
            location = request.POST.get('location')

            name = name.title()
            location = location.title()

            # Check password strength
            if not is_password_strong(password):
                messages.warning(request, "Password does not meet strength requirements.")
                return render(request, self.template_name)

            # Check for forbidden words in the password
            forbidden_words = ['password', '123456', 'qwerty']
            for word in forbidden_words:
                if word.lower() in password.lower():
                    messages.warning(request, "Password contains forbidden word(s).")
                    return render(request, self.template_name)

            # Define a regular expression pattern to match only digits
            pattern = r'^\d{10,11}$'

            # Check if the mobile number matches the pattern
            if not re.match(pattern, mobile) or len(mobile) > 10 or len(mobile) < 10:
                messages.warning(request, "Mobile number should contain only digits and be 10 or 11 digits long.")
                return render(request, self.template_name)

            if JobSeeker.objects.filter(email_id=email).exists():
                messages.warning(request, "User with this email already exists.")
            else:
                # Hash the password before storing it
                hashed_password = make_password(password)

                new_job_seeker = JobSeeker(full_name=name, email_id=email, mobile_no=mobile, password=hashed_password,
                                           location=location)

                # Save the new user to the database
                new_job_seeker.save()

                return redirect('login')
        except ValidationError as e:
            messages.warning(request, f"Fail: {str(e)}")

        return render(request, self.template_name)
