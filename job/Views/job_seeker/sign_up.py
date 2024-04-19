import random
import re
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.views import generic, View
from job.models import JobSeeker, Job
from job.utils import *
from django.contrib import messages
from django.core.exceptions import ValidationError


def u_generate_otp():
    return ''.join(random.choices('0123456789', k=8))  # Generate a 8-digit OTP


def u_send_otp(otp, email):
    message_body = (f"Dear User,\n\nThank you for registering with our platform. Your OTP for verification is: {otp}."
                    f"\n\nPlease use this OTP to complete your registration process.\n\nBest regards,\nThe Jobs4U Team")
    email_message = EmailMessage("Otp for Verification", message_body, to=[email])
    email_message.send()


def u_send_email(name, email):
    messages_body = (f"""
            Dear {name},

            We are thrilled to welcome you to the Jobs4U community!\n 
            Your registration is now complete, and you're officially part of a vibrant network dedicated to connecting 
            talented individuals like yourself with exciting career opportunities.

            At Jobs4U, our mission is to empower job seekers in finding their dream roles while assisting employers in 
            discovering top-tier talent. We're committed to providing you with a seamless and rewarding job search experience.

            *Real-Time Updates:* Stay informed about the latest job postings, application status updates, and networking 
            events through our regular email notifications. 
            You'll never miss out on an opportunity that could propel your career forward.\n

            Your journey towards a fulfilling career starts now, and we're honored to be a part of it. 
            Should you have any questions or need assistance, please don't hesitate to reach out to our dedicated support 
            team at [support@email.com].

            Once again, welcome to Jobs4U! We're excited to embark on this journey with you and witness your success unfold.\n

            Best Regards,
            Jobs4U Team
        """)

    email_message = EmailMessage("Welcome to [Job Portal Name] - Your Journey Starts Here!", messages_body, to=[email])
    email_message.send()


class UserSignupView(View):
    template_name = 'job_seeker/UserR.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:

            # Get form data from POST request
            name = request.POST.get('name')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            password = request.POST.get('pwd')
            location = request.POST.get('location')
            city = request.POST.get('city')

            name = name.title()
            city = city.title()

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
            if not re.match(pattern, mobile) or len(mobile) != 10:
                messages.error(request, "Mobile number should contain only digits and be 10 digits long.")
                return render(request, self.template_name)

            if User.objects.filter(username=email).exists():
                messages.warning(request, "User with this email already exists.")
                return render(request, self.template_name)

            # Save user details temporarily (in session)
            request.session['temp_user_details'] = {
                'name': name,
                'email': email,
                'mobile': mobile,
                'password': password,
                'location': location,
                'city': city,
            }

            # Generate OTP
            otp = u_generate_otp()
            print(otp)

            # Send OTP via SMS
            u_send_otp(otp, email)

            messages.info(request, "OTP for verification sent to email")

            # Store the OTP in session
            request.session['otp'] = otp
            request.session['verified_email'] = email

            # Render a template with a form to enter OTP for verification
            return render(request, 'job_seeker/u_verify_otp.html')

        except ValidationError as e:
            messages.error(request, f"Fail: {str(e)}")

        return render(request, self.template_name)


def verify_otp_view_u(request):
    if request.method == 'POST':
        otp_entered = request.POST.get('otp')
        stored_otp = request.session.get('otp')

        print(otp_entered)
        print(stored_otp)

        if otp_entered == stored_otp:
            # If OTP is verified successfully, proceed with user creation
            # Retrieve user details from session or temporary storage
            user_details = request.session.get('temp_user_details')

            # Create new User object
            new_user = User.objects.create_user(username=user_details['email'], password=user_details['password'])
            new_user.save()

            # Create new Recruiter object
            new_seeker = JobSeeker(
                full_name=user_details['name'],
                email_id=user_details['email'],
                mobile_no=user_details['mobile'],
                address=user_details['location'],
                city=user_details['city'],
                user=new_user
            )
            new_seeker.save()

            u_send_email(user_details['name'], user_details['email'])

            # Clear session data
            del request.session['otp']
            del request.session['verified_email']
            del request.session['temp_user_details']

            messages.success(request, 'Signup success')
            return redirect('login')
        else:
            messages.error(request, 'Invalid OTP, please try again.')
            return redirect('u_verify')  # Redirect back to signup page

    return render(request, 'job_seeker/u_verify_otp.html')


def u_landing_page(request):
    logged_in_user_id = request.session.get('logged_in_user_id')

    if logged_in_user_id:
        try:
            job_seeker = JobSeeker.objects.get(id=logged_in_user_id)
            return render(request, 'job_seeker/u_landing_page.html', {'job_seeker': job_seeker})
        except JobSeeker.DoesNotExist:
            # Handle case where no JobSeeker instance is found for the logged-in user
            return render(request, 'landing_page.html', {'error': 'JobSeeker instance not found'})
    else:
        # User is not logged in, handle accordingly
        return redirect('login')


def u_landing_filter(request):
    options = Job.objects.order_by('location').values_list('location', flat=True).distinct()
    print(options)
    return render(request, 'job_seeker/u_landing_page.html', {'options': options})

