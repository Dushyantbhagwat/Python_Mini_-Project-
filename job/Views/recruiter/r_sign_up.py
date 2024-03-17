from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views import View
import re
from job.models import Recruiter
from job.utils import *
from django.contrib.auth.models import User


from django.contrib.auth.models import User


class RecruiterSignupView(View):
    template_name = 'recruiter/RecruiterRegistration.html' # class variable

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            company = request.POST.get('company')
            contact = request.POST.get('mobile')
            website = request.POST.get('website')
            password = request.POST.get('password')

            name = name.title()

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
            if not re.match(pattern, contact) or len(contact) != 10:
                messages.error(request, "Mobile number should contain only digits and be 10 digits long.")
                return render(request, self.template_name)

            if User.objects.filter(username=email).exists():
                messages.warning(request, "User with this email already exists.")
                return render(request, self.template_name)

            # Create new User object
            new_user = User.objects.create_user(username=email,  password=password)
            new_user.save()

            # Create new Recruiter object
            new_recruiter = Recruiter(full_name=name, email_id=email, mobile=contact,
                                       company_name=company, website=website, user=new_user)
            new_recruiter.save()

            messages.success(request, 'Signup success')
            return redirect('login')

        except ValidationError as e:
            messages.error(request, f"Fail: {str(e)}")

        return render(request, self.template_name)

