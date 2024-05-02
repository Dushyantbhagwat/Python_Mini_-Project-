import http.client

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.views import View
import re
from job.models import Recruiter
from job.utils import *
from django.contrib.auth.models import User
import random
# from twilio.rest import Client
# from twilio.base.client_base import TwilioClient

from django.contrib.auth.models import User
# import requests

from django.conf import settings


# class RecruiterSignupView(View):
#     template_name = 'recruiter/RecruiterRegistration.html' # class variable
#
#     def get(self, request):
#         return render(request, self.template_name)
#
#     def post(self, request):
#         try:
#             name = request.POST.get('name')
#             email = request.POST.get('email')
#             company = request.POST.get('company')
#             contact = request.POST.get('mobile')
#             website = request.POST.get('website')
#             password = request.POST.get('password')
#
#             name = name.title()
#
#             # Check password strength
#             if not is_password_strong(password):
#                 messages.warning(request, "Password does not meet strength requirements.")
#                 return render(request, self.template_name)
#
#             # Check for forbidden words in the password
#             forbidden_words = ['password', '123456', 'qwerty']
#             for word in forbidden_words:
#                 if word.lower() in password.lower():
#                     messages.warning(request, "Password contains forbidden word(s).")
#                     return render(request, self.template_name)
#
#             # Define a regular expression pattern to match only digits
#             pattern = r'^\d{10,11}$'
#
#             # Check if the mobile number matches the pattern
#             if not re.match(pattern, contact) or len(contact) != 10:
#                 messages.error(request, "Mobile number should contain only digits and be 10 digits long.")
#                 return render(request, self.template_name)
#
#             if User.objects.filter(username=email).exists():
#                 messages.warning(request, "User with this email already exists.")
#                 return render(request, self.template_name)
#
#             # Create new User object
#             new_user = User.objects.create_user(username=email,  password=password)
#             new_user.save()
#
#             # Create new Recruiter object
#             new_recruiter = Recruiter(full_name=name, email_id=email, mobile=contact,
#                                        company_name=company, website=website, user=new_user)
#             new_recruiter.save()
#
#             messages.success(request, 'Signup success')
#             return redirect('login')
#
#         except ValidationError as e:
#             messages.error(request, f"Fail: {str(e)}")
#
#         return render(request, self.template_name)


def r_generate_otp():
    return ''.join(random.choices('0123456789', k=8))  # Generate a 8-digit OTP


def r_send_otp(otp, email):
    message_body = (f"Dear User,\n\nThank you for registering with our platform. Your OTP for verification is: {otp}."
                    f"\n\nPlease use this OTP to complete your registration process.\n\nBest regards,\nThe Jobs4U Team")
    email_message = EmailMessage("Otp for Verification", message_body, to=[email])
    email_message.send()


def r_send_email(name, email):
    messages_body = (f"""

        Dear {name},

        We are thrilled to welcome you to Jobs4U! Thank you for registering as a recruiter on our platform. 
        Your interest in connecting with top talent is greatly appreciated.

        Your account details are as follows:
        - Username: {email}

        Please note that your account is currently pending approval. Access to our job portal will be granted only after administrative review and approval. Once approved, you will have full access to our platform's features, including the ability to post job listings, search for candidates, and manage your recruitment activities efficiently.

        We will notify you via email as soon as your account is approved. If you have any questions or need assistance, please don't hesitate to reach out to our support team at [Support Email Address].

        Thank you again for choosing Jobs4U. We look forward to helping you find the perfect candidates for your open positions.

        Best regards,
        Jobs4U Team

    """)

    email_message = EmailMessage("Welcome to Jobs4U - Account Registration Confirmation", messages_body, to=[email])
    email_message.send()


class RecruiterSignupView(View):
    template_name = 'recruiter/RecruiterRegistration.html'  # class variable

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

            # Save user details temporarily (in session)
            request.session['temp_user_details'] = {
                'name': name,
                'email': email,
                'company': company,
                'contact': contact,
                'website': website,
                'password': password,
            }

            # Generate OTP
            otp = r_generate_otp()
            print(otp)

            # Send OTP via SMS
            r_send_otp(otp, email)

            # Store the OTP in session
            request.session['otp'] = otp
            request.session['verified_mobile'] = contact

            # Render a template with a form to enter OTP for verification
            return render(request, 'recruiter/verify_otp.html')

        except ValidationError as e:
            messages.error(request, f"Fail: {str(e)}")

        return render(request, self.template_name)


def verify_otp_view(request):
    if request.method == 'POST':
        otp_entered = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        # verified_mobile = request.session.get('verified_mobile')

        if otp_entered == stored_otp:
            # If OTP is verified successfully, proceed with user creation
            # Retrieve user details from session or temporary storage
            user_details = request.session.get('temp_user_details')

            # Create new User object
            new_user = User.objects.create_user(username=user_details['email'], password=user_details['password'])
            new_user.save()

            # Create new Recruiter object
            new_recruiter = Recruiter(
                full_name=user_details['name'],
                email_id=user_details['email'],
                mobile=user_details['contact'],
                company_name=user_details['company'],
                website=user_details['website'],
                user=new_user
            )
            new_recruiter.save()

            r_send_email(user_details['name'], user_details['email'])

            # Clear session data
            del request.session['otp']
            del request.session['verified_mobile']
            del request.session['temp_user_details']

            messages.success(request, 'Signup success')
            return redirect('login')
        else:
            messages.error(request, 'Invalid OTP, please try again.')
            return redirect('r_signup')  # Redirect back to signup page

    return render(request, 'recruiter/verify_otp.html')


def u_landing_page(request):
    logged_in_user_id = request.session.get('logged_in_user_id')

    if logged_in_user_id:
        try:
            recruiter = Recruiter.objects.get(id=logged_in_user_id)
            return render(request, 'recruiter/RLandingPage.html', {'recruiter': recruiter})
        except Recruiter.DoesNotExist:
            # Handle case where no JobSeeker instance is found for the logged-in user
            return render(request, 'landing_page.html', {'error': 'Recruiter instance not found'})
    else:
        # User is not logged in, handle accordingly
        messages.warning(request, "Please Login to the Portal first!")
        return redirect('login')








