from django.shortcuts import render


def post_jobs(request, r_id):
    context = {'r_id': r_id}
    return render(request, 'recruiter/PostJobs.html', context)

