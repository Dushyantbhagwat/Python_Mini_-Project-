import datetime

from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.views import generic
from job.models import Job, Recruiter, JobSeeker, Application
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from django.db.models import Count


def job_list(request):
    jobs = Job.objects.all()
    # i = [job.recruiter_id for job in jobs]
    # print(i)

    # Retrieve a list of unique cities ordered alphabetically
    # options = Job.objects.values('city').annotate(city_count=Count('city')).order_by('city').distinct()
    options = Job.objects.order_by('location').values_list('location', flat=True).distinct()
    skill_options = Job.objects.order_by('skills').values_list('skills', flat=True).distinct()
    title_options = Job.objects.order_by('title').values_list('title', flat=True).distinct()
    print(options, skill_options, title_options)

    context = {'jobs': jobs, 'options': options, 'skill_options': skill_options, 'title_options': title_options}
    # print(options)
    return render(request, 'job_seeker/JList.html', context=context)


def job_details(request, job_id):
    jobs = get_object_or_404(Job, id=job_id)

    logged_in_user_id = request.session.get('logged_in_user_id')
    print(logged_in_user_id)

    if logged_in_user_id:
        try:
            job_seeker = JobSeeker.objects.get(id=logged_in_user_id)
            print(job_seeker.id)
        except JobSeeker.DoesNotExist:
            messages.warning(request, "Please Login to the Portal")
            return render(request, 'landing_page.html', {'error': 'JobSeeker instance not found'})
    else:
        return redirect('login')

    return render(request, 'job_seeker/JobDetails.html', {'jobs': jobs, 'job_seeker': job_seeker})


def job_detail_email(email_id, job):
    subject = f"Job Application Details for {job.title}"
    message_body = f"Company Name: {job.recruiter.company_name}\n"
    message_body += f"Job Description: {job.description}\n"
    message_body += f"Location: {job.location}\n"
    # Add more job details as needed

    email_message = EmailMessage(subject, message_body, to=[email_id])
    email_message.send()


def apply(request):
    if request.method == 'POST':
        logged_in_user_id = request.session.get('logged_in_user_id')

        # Check if the user has already applied for more than 5 jobs
        if Application.objects.filter(user_id=logged_in_user_id).count() > 4:
            messages.warning(request, "You have already applied for more than 5 jobs.")
            return redirect('job_list')

        job_id = request.POST.get('job_id')
        print(job_id)

        # Check if the user has already applied for this job
        if Application.objects.filter(user_id=logged_in_user_id, job_id=job_id).exists():
            messages.warning(request, "You have already applied for this job.")
            return redirect('job_list')

        date = datetime.datetime.now()

        job_seeker = JobSeeker.objects.get(id=logged_in_user_id)
        print(job_seeker.id)

        # Check if the user has uploaded the resume or not
        if job_seeker.resume == 'not uploaded':
            messages.warning(request, "Please first upload your resume!")
            return redirect('u_profile')

        job = get_object_or_404(Job, id=job_id)  # Fetch the Job instance corresponding to job_id
        print(job.id)

        try:
            application = Application.objects.create(date=date, user=job_seeker, job=job)
            application.save()
            messages.success(request, "Job Application Process Successful!")
            return HttpResponseRedirect(reverse('job_list'))  # Redirect to a success page
        except JobSeeker.DoesNotExist:
            messages.warning(request, "Please Login to the Portal")
            return render(request, 'u_landing_page.html', {'message': 'Job Seeker not found'}, status=404)

    else:
        return HttpResponseNotAllowed(['POST'])  # Return method not allowed response for non-POST requests


def job_status(request):
    logged_in_user_id = request.session.get('logged_in_user_id')

    # Assuming JobSeeker is your model for job_seekers
    job_seeker = JobSeeker.objects.get(id=logged_in_user_id)

    # Fetch all applications associated with the job_seeker
    applications = Application.objects.filter(user=job_seeker)

    # Now, let's iterate over each application and extract the associated job and status
    jobs = []
    for application in applications:
        job = application.job
        status = application.status  # Assuming status is a field in your Application model
        date = application.date
        reason = application.reason
        jobs.append((job, status, date, reason))

    # Now, 'jobs' contains tuples of (job, status) applied to by the job_seeker
    print(jobs)

    return render(request, 'job_seeker/JobStatus.html', {'jobs': jobs})


def job_accepted(request):
    logged_in_user_id = request.session.get('logged_in_user_id')

    # Assuming JobSeeker is your model for job_seekers
    job_seeker = JobSeeker.objects.get(id=logged_in_user_id)

    # Fetch all applications associated with the job_seeker
    applications = Application.objects.filter(user=job_seeker)

    # Now, let's iterate over each application and extract the associated job and status
    jobs = []
    for application in applications:
        if application.status == 'Accepted':
            job = application.job
            status = application.status  # Assuming status is a field in your Application model
            date = application.date
            reason = application.reason
            jobs.append((job, status, date, reason))

    # Now, 'jobs' contains tuples of (job, status) applied to by the job_seeker
    print(jobs)

    return render(request, 'job_seeker/JobStatus.html', {'jobs': jobs})


def job_rejected(request):
    logged_in_user_id = request.session.get('logged_in_user_id')

    # Assuming JobSeeker is your model for job_seekers
    job_seeker = JobSeeker.objects.get(id=logged_in_user_id)

    # Fetch all applications associated with the job_seeker
    applications = Application.objects.filter(user=job_seeker)

    # Now, let's iterate over each application and extract the associated job and status
    jobs = []
    for application in applications:
        if application.status == 'Rejected':
            job = application.job
            status = application.status  # Assuming status is a field in your Application model
            date = application.date
            reason = application.reason
            jobs.append((job, status, date, reason))

    # Now, 'jobs' contains tuples of (job, status) applied to by the job_seeker
    print(jobs)

    return render(request, 'job_seeker/JobStatus.html', {'jobs': jobs})
