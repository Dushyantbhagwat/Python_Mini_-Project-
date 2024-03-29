from django.shortcuts import render


def post_jobs(request):
    return render(request, 'recruiter/PostJobs.html')

# recruiter.session