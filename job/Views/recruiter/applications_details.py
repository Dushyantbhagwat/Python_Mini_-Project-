from django.shortcuts import render

from job.models import Job, Application, JobSeeker


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


# views.py

from django.http import JsonResponse

def search_resumes(request):
    if request.method == 'GET' and request.is_ajax():
        search_text = request.GET.get('search_text', '')

        # Filter applications based on resume content
        matching_applications = Application.objects.filter(
            user__resume_content__icontains=search_text
        )

        # Serialize the matching applications to JSON
        matching_applications_data = [{
            'id': app.id,
            'full_name': app.user.full_name,
            # Add other fields you want to include in the response
        } for app in matching_applications]

        return JsonResponse({'matching_applications': matching_applications_data})

    # Return empty response if request method is not GET or not AJAX
    return JsonResponse({})
