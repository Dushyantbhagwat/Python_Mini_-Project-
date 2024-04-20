from django.shortcuts import render

from job.models import Job, Application


def application(request, app_id):

    # Retrieve the application from the database
    try:
        apps = Application.objects.get(id=app_id)
    except Application.DoesNotExist:
        # Handle the case where the application does not exist
        # For example, you could render a 404 page
        return render(request, '404.html')

    # Access the job ID associated with the application
    job_id = apps.job_id

    jobs = Job.objects.filter(id=job_id)

    for job in jobs:
        title = job.title
        print(title)
        description = job.description
        type = job.job_type
        salary = job.minimum_salary
        end_date = job.deadline
        location = job.location
        skills = job.skills
        start_date = job.start_date
        experience = job.experience

    return render(request, 'recruiter/Application.html', {'job': job})

