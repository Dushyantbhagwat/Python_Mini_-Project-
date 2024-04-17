import datetime

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
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
            return render(request, 'landing_page.html', {'error': 'JobSeeker instance not found'})
    else:
        return redirect('login')

    return render(request, 'job_seeker/JobDetails.html', {'jobs': jobs, 'job_seeker': job_seeker})


def apply(request):
    if request.method == 'POST':
        logged_in_user_id = request.session.get('logged_in_user_id')

        job_id = request.POST.get('job_id')
        print(job_id)

        date = datetime.datetime.now()

        job_seeker = JobSeeker.objects.get(id=logged_in_user_id)
        print(job_seeker.id)

        # if job_seeker.resume == 'not uploaded':
        #     messages.warning(request, "Please first upload your resume!")
        #     return redirect('u_profile')

        job = get_object_or_404(Job, id=job_id)  # Fetch the Job instance corresponding to job_id
        print(job.id)

        try:
            application = Application.objects.create(date=date, user=job_seeker, job=job)
            application.save()
            messages.success(request, "Job Application Process Successful!")
            return HttpResponseRedirect(reverse('job_list'))  # Redirect to a success page
        except JobSeeker.DoesNotExist:
            return render(request, 'landing_page.html', {'message': 'Job Seeker not found'}, status=404)

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
        jobs.append((job, status, date))

    # Now, 'jobs' contains tuples of (job, status) applied to by the job_seeker
    print(jobs)

    return render(request, 'job_seeker/JobStatus.html', {'jobs': jobs})

