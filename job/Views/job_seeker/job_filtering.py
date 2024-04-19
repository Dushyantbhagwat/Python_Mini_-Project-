import datetime

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
from job.models import Job
from functools import reduce
from operator import or_

from django.db.models import Q


def filter_jobs(request):
    if request.method == 'POST':
        # Retrieve filter options from the request
        job_type_filter = request.POST.get('jobTypeFilter')
        experience_filter = request.POST.get('experienceRangeFilter')
        salary_filter = request.POST.get('salaryRangeFilter')
        city_filter = request.POST.get('locationFilter')
        skills_filter = request.POST.get('skillsFilter')
        title_filter = request.POST.get('titleFilter')
        date_filter = request.POST.get('dateFilter')

        print(job_type_filter, experience_filter, salary_filter, city_filter, skills_filter, date_filter)

        # Initialize an empty list to store filter conditions
        filter_conditions = []

        if (job_type_filter == 'All' or experience_filter == 'All' or salary_filter == 'All' or city_filter == 'All' or
                skills_filter == 'All' or title_filter == 'All' or date_filter == 'All'):
            jobs = Job.objects.all()
            options = Job.objects.order_by('location').values_list('location', flat=True).distinct()
            skill_options = Job.objects.order_by('skills').values_list('skills', flat=True).distinct()
            title_options = Job.objects.order_by('title').values_list('title', flat=True).distinct()
            print(options, skill_options, title_options)
            print(experience_filter)
            context = {'jobs': jobs, 'options': options, 'skill_options': skill_options, 'title_options': title_options}
            return render(request, 'job_seeker/JList.html', context=context)

        else:
            # Check if each condition is provided and add it to the filter_conditions list
            if job_type_filter:
                filter_conditions.append(('job_type', job_type_filter))

            if experience_filter:
                filter_conditions.append(('experience', experience_filter))

            # Handle salary range filter
            if salary_filter:
                min_salary, max_salary = map(int, salary_filter.split('-'))
                print(min_salary, max_salary)
                filter_conditions.append(Q(minimum_salary__lte=max_salary))

            if city_filter:
                filter_conditions.append(('location', city_filter))

            if skills_filter:
                filter_conditions.append(('skills', skills_filter))

            if title_filter:
                filter_conditions.append(('title', title_filter))

            if date_filter:
                filter_conditions.append(Q(deadline=date_filter))

            # Start with all jobs and progressively filter based on provided conditions
            jobs = Job.objects.all()
            options = Job.objects.order_by('location').values_list('location', flat=True).distinct()
            skill_options = Job.objects.order_by('skills').values_list('skills', flat=True).distinct()
            title_options = Job.objects.order_by('title').values_list('title', flat=True).distinct()
            print(options, skill_options, title_options)

            if filter_conditions:
                # Construct filter query dynamically based on the provided conditions
                filter_query = Q()
                for condition in filter_conditions:
                    if isinstance(condition, Q):
                        filter_query &= condition
                    else:
                        filter_query &= Q(**{condition[0]: condition[1]})

                # Apply filter query to jobs
                jobs = jobs.filter(filter_query)

            context = {'jobs': jobs, 'options': options, 'skill_options': skill_options, 'title_options': title_options}

            # Render a new page with the filtered jobs
            return render(request, 'job_seeker/JList.html', context=context)
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




















