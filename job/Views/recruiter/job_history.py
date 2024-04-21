import datetime

from django.http import HttpResponse

from job.models import Recruiter, Job, Application
from django.shortcuts import render, get_object_or_404


def jobs_history(request):
    logged_in_user_id = request.session.get('logged_in_user_id')

    # Check if the logged-in user is a recruiter
    try:
        recruiter = Recruiter.objects.get(id=logged_in_user_id)
    except Recruiter.DoesNotExist:
        return HttpResponse("Recruiter not found.")

    jobs = Job.objects.filter(recruiter=recruiter)

    for job in jobs:
        # Count applications for each status
        job.total_applications = Application.objects.filter(job=job).count()
        job.total_accepted = Application.objects.filter(job=job, status='Accepted').count()
        job.total_rejected = Application.objects.filter(job=job, status='Rejected').count()
        job.total_pending = Application.objects.filter(job=job, status='Pending').count()

    context = {
        'jobs': jobs,
    }

    return render(request, 'recruiter/JobHistory.html', context=context)




# def jobs_history(request):
#     logged_in_user_id = request.session.get('logged_in_user_id')
#
#     recruiter = get_object_or_404(Recruiter, id=logged_in_user_id)
#
#     jobs = Job.objects.filter(recruiter=recruiter.id)
#
#     total_applications = 0
#     total_pending = 0
#     total_accepted = 0
#     total_rejected = 0
#
#     for job in jobs:
#         job_applications = job.application_set.all()
#         total_applications += job_applications.count()
#         total_pending += job_applications.filter(status='Pending').count()
#         total_accepted += job_applications.filter(status='Accepted').count()
#         total_rejected += job_applications.filter(status='Rejected').count()
#
#     print("Total Applications:", total_applications)
#     print("Total Pending:", total_pending)
#     print("Total Accepted:", total_accepted)
#     print("Total Rejected:", total_rejected)
#
#     context = {
#         'jobs': jobs,
#         'total_applications': total_applications,
#         'total_pending': total_pending,
#         'total_accepted': total_accepted,
#         'total_rejected': total_rejected,
#     }
#
#     return render(request, 'recruiter/JobHistory.html', context=context)


