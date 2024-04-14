from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
from job.models import Job


def filter_jobs(request):
    if request.method == 'POST':
        # Retrieve filter options from the request
        job_type_filter = request.POST.get('job_type')

        # Filter jobs based on the selected filter options
        if job_type_filter == 'all':
            filtered_jobs = Job.objects.all()  # Get all jobs
        else:
            filtered_jobs = Job.objects.filter(job_type=job_type_filter)  # Filter jobs by job type
            print(filtered_jobs)

        # Serialize filtered job data

        # Return filtered data as a JSON response
        return render(request, 'job_seeker/JList.html', {'jobs': filtered_jobs})
    else:
        print('error')
        # Handle invalid requests
        return JsonResponse({'error': 'Invalid request'}, status=400)


















# class LandingFilter(generic.TemplateView):
#     template_name = 'JList.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Retrieve data from the database
#         options = Job.objects.order_by('city').values_list('city', flat=True).distinct()
#         print(f"{options}")
#         context['options'] = options
#         print(context)
#         return context


# def filter_job(request):
#     if request.method == 'POST':
#         # experience = request.POST.get('experience')
#         job_type = request.POST.get('jobTypeFilter')
#         # city = request.POST.get('city')
#
#         # Start with all jobs and progressively filter based on provided criteria
#         jobs = Job.objects.all()
#
#         # if experience:
#         #     # Assuming experience is stored as an integer field in Job model
#         #     jobs = jobs.filter(experience=experience)  # Filter jobs with experience greater than or equal to provided value
#
#         if job_type:
#             jobs = jobs.filter(job_type=job_type)  # Filter jobs by job type
#
#         # if city:
#         #     jobs = jobs.filter(city=city)  # Filter jobs by city
#
#         # Pass filtered jobs to the template context
#         return render(request, 'job_seeker/JList.html', {'jobs': jobs})
#
#     return render(request, 'job_seeker/JList.html')
#
#
# def all_filter_job(request):
#     if request.method == 'POST':
#         experience = request.POST.get('experience')
#         job_type = request.POST.get('job_type')
#         city = request.POST.get('city')
#
#         print(experience, job_type, city)
#
#         # Start with all jobs and progressively filter based on provided criteria
#         jobs = Job.objects.all()
#
#         if experience:
#             # Assuming experience is stored as an integer field in Job model
#             jobs = jobs.filter(experience=experience)  # Filter jobs with experience greater than or equal to provided value
#
#         if job_type:
#             jobs = jobs.filter(job_type=job_type)  # Filter jobs by job type
#
#         if city:
#             jobs = jobs.filter(city=city)  # Filter jobs by city
#
#         # Pass filtered jobs to the template context
#         return render(request, 'job_seeker/JList.html', {'jobs': jobs})
#
#     return render(request, 'job_seeker/JList.html')






# def all_filter_job(request):
#     if request.method == 'POST':
#         experience = request.POST.get('experience')
#         job_type = request.POST.get('job_type')
#         city = request.POST.get('city')
#
#         print(experience, job_type, city)
#
#         # Initialize an empty list to store filter conditions
#         filter_conditions = []
#
#         # Check if each condition is provided and add it to the filter_conditions list
#         if experience:
#             filter_conditions.append(('experience', experience))
#
#         if job_type:
#             filter_conditions.append(('job_type', job_type))
#
#         if city:
#             filter_conditions.append(('city', city))
#
#         # Start with all jobs and progressively filter based on provided conditions
#         jobs = Job.objects.all()
#
#         # Ensure at least three conditions are provided
#         if len(filter_conditions) >= 3:
#             # Construct filter query dynamically based on the provided conditions
#             filter_query = {condition[0]: condition[1] for condition in filter_conditions[:3]}
#
#             # Apply filter query to jobs
#             jobs = jobs.filter(**filter_query)
#
#             # Render a new page with the filtered jobs
#             return render(request, 'job_seeker/JList.html', {'jobs': jobs})
#
#     # If request method is not POST or if there are fewer than three filtering criteria provided, render the default page
#     return render(request, 'job_seeker/JList.html')




















