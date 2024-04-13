from datetime import datetime

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from job.models import Job, Recruiter
from django.utils import timezone
from django.utils.dateparse import parse_datetime

# def post_jobs(request, r_id):
#     context = {'r_id': r_id}
#
#     if request.method == 'POST':
#         try:
#             job_title = request.POST.get('job_title')
#             description = request.POST.get('job_description')
#             location = request.POST.get('location')
#             start_date = request.POST.get('start_date')
#             end_date = request.POST.get('end_date')
#             job_type = request.POST.get('selected_job_type')
#             minimum_salary = request.POST.get('minimum')
#             maximum_salary = request.POST.get('maximum')
#             experience = request.POST.get('experience')
#             skills = request.POST.get('skills')
#
#             # Print the received data
#             print(job_title, description, location, start_date, end_date, job_type, maximum_salary, minimum_salary,
#                   experience, skills)
#
#
#
#             # Title case conversion for certain fields
#             job_title = job_title.title()
#             description = description.title()
#             location = location.title()
#             skills = skills.title()
#
#             # Splitting date-time strings
#             start_date = start_date.split('T')[0]  # Extract date part only
#             end_date = end_date.split('T')[0]  # Extract date part only
#
#             # Fetching the recruiter object based on r_id
#             recruiter = Recruiter.objects.get(id=r_id)
#
#             # Create the Job object with the related recruiter
#             job = Job.objects.create(
#                 title=job_title,
#                 description=description,
#                 location=location,
#                 start_date=start_date,
#                 deadline=end_date,
#                 job_type=job_type,
#                 maximum_salary=maximum_salary,
#                 experience=experience,
#                 skills=skills,
#                 recruiter=recruiter  # Assign the recruiter object
#             )
#
#             # Notify user of successful job posting
#             messages.success(request, 'Job Posted Successfully!')
#             return redirect('r_profile', recruiter=r_id)
#
#         except ValidationError as e:
#             # Notify user of validation error
#             messages.error(request, f"Failed to post job: {str(e)}")
#             return render(request, 'recruiter/PostJobs.html', context)
#
#     return render(request, 'recruiter/PostJobs.html', context)
#
#
# def post_jobs(request, r_id):
#     context = {'r_id': r_id}
#
#     if request.method == 'POST':
#         try:
#             job_title = request.POST.get('job_title')
#             description = request.POST.get('job_description')
#             location = request.POST.get('location')
#             start_date = request.POST.get('start_date')
#             end_date = request.POST.get('end_date')
#             job_type = request.POST.get('selected_job_type')
#             minimum_salary = request.POST.get('minimum')
#             maximum_salary = request.POST.get('maximum')
#             experience = request.POST.get('experience')
#             skills = request.POST.get('skills')
#
#             # Print the received data
#             print(job_title, description, location, start_date, end_date, job_type, maximum_salary, minimum_salary,
#                   experience, skills)
#
#             # Title case conversion for certain fields
#             job_title = job_title.title()
#             description = description.title()
#             location = location.title()
#             skills = skills.title()
#
#             # Splitting date-time strings
#             # start_date = start_date.split('T')[0]  # Extract date part only
#             # end_date = end_date.split('T')[0]  # Extract date part only
#
#             start_date = start_date.split('T')
#             end_date = end_date.split('T')
#
#             # Fetching the recruiter object based on r_id
#             recruiter = Recruiter.objects.get(id=r_id)
#
#             # Create the Job object with the related recruiter
#             job = Job.objects.create(
#                 title=job_title,
#                 description=description,
#                 location=location,
#                 start_date=start_date,
#                 deadline=end_date,
#                 job_type=job_type,
#                 maximum_salary=maximum_salary,
#                 experience=experience,
#                 skills=skills,
#                 recruiter=recruiter  # Assign the recruiter object
#             )
#
#             # Notify user of successful job posting
#             messages.success(request, 'Job Posted Successfully!')
#             return redirect('r_profile')
#
#         except ValidationError as e:
#             # Notify user of validation error
#             messages.error(request, f"Failed to post job: {str(e)}")
#             return render(request, 'recruiter/PostJobs.html', context)
#
#     return render(request, 'recruiter/PostJobs.html', context)

from django.utils import timezone


def post_jobs(request):
    # context = {'r_id': r_id}

    logged_in_user_id = request.session.get('logged_in_user_id')
    r_id = Recruiter.objects.get(id=logged_in_user_id)

    if request.method == 'POST':
        try:
            # Retrieve job data from POST request
            job_title = request.POST.get('job_title')
            description = request.POST.get('job_description')
            location = request.POST.get('location')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            job_type = request.POST.get('selected_job_type')
            minimum_salary = request.POST.get('minimum')
            maximum_salary = request.POST.get('maximum')
            experience = request.POST.get('experience')
            skills = request.POST.get('skills')
            rate = request.POST.get('rate')

            print(rate, job_type, maximum_salary)

            # Title case conversion for certain fields
            job_title = job_title.title()
            description = description.title()
            location = location.title()
            skills = skills.title()

            # Splitting date-time strings
            start_date = start_date.split('T')[0]  # Extract date part only
            end_date = end_date.split('T')[0]  # Extract date part only

            # Convert string dates to datetime objects
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

            # Check if start date is after or equal to today's date
            if start_date < timezone.now().date() or end_date <= timezone.now().date():
                messages.error(request, 'Date must be after or equal to today')
                return render(request, 'recruiter/PostJobs.html')

            if start_date == end_date:
                messages.error(request, "opening date can't be same as deadline date")
                return redirect('post_jobs')

            if start_date > end_date:
                messages.error(request, "start date must be before deadline")
                return redirect('post_jobs')

            # Fetching the recruiter object based on r_id
            recruiter = Recruiter.objects.get(id=r_id.id)

            # Create the Job object with the related recruiter
            job = Job.objects.create(
                title=job_title,
                description=description,
                location=location,
                start_date=start_date,
                deadline=end_date,
                job_type=job_type,
                maximum_salary=maximum_salary,
                minimum_salary=minimum_salary,
                experience=experience,
                skills=skills,
                rate=rate,
                recruiter=recruiter  # Assign the recruiter object
            )

            # Notify user of successful job posting
            messages.success(request, 'Job Posted Successfully!')

            # Redirect to recruiter profile
            return redirect('post_jobs')

        except ValidationError as e:
            # Notify user of validation error
            messages.error(request, f"Failed to post job: {str(e)}")
            return render(request, 'recruiter/PostJobs.html')

    # Render the same view if request method is not POST
    return render(request, 'recruiter/PostJobs.html',)



