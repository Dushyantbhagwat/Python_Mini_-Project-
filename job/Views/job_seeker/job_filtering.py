from django.shortcuts import render
from django.views import generic

from job.models import Job


class LandingFilter(generic.TemplateView):
    template_name = 'JList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve data from the database
        options = Job.objects.order_by('city').values_list('city', flat=True).distinct()
        print(f"{options}")
        context['options'] = options
        print(context)
        return context


def filter_job(request):
    if request.method == 'POST':
        experience = request.POST.get('experience')
        job_type = request.POST.get('job_type')
        city = request.POST.get('city')

        # Start with all jobs and progressively filter based on provided criteria
        jobs = Job.objects.all()

        if experience:
            # Assuming experience is stored as an integer field in Job model
            jobs = jobs.filter(experience=experience)  # Filter jobs with experience greater than or equal to provided value

        if job_type:
            jobs = jobs.filter(job_type=job_type)  # Filter jobs by job type

        if city:
            jobs = jobs.filter(city=city)  # Filter jobs by city

        # Pass filtered jobs to the template context
        return render(request, 'job_seeker/JList.html', {'jobs': jobs})

    return render(request, 'job_seeker/JList.html')
