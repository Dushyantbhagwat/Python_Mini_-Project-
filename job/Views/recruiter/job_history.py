from django.shortcuts import render

from job.models import Recruiter, Job, Application


def jobs_history(request):
    logged_in_user_id = request.session.get('logged_in_user_id')

    recruiter = Recruiter.objects.get(id=logged_in_user_id)

    jobs = Job.objects.filter(recruiter=recruiter.id)

    total_applications = 0
    total_pending = 0
    total_accepted = 0
    total_rejected = 0

    for job in jobs:
        job_applications = job.application_set.all()
        total_applications += job_applications.count()
        total_pending += job_applications.filter(status='request pending').count()
        total_accepted += job_applications.filter(status='accepted').count()
        total_rejected += job_applications.filter(status='rejected').count()

    print("Total Applications:", total_applications)
    print("Total Pending:", total_pending)
    print("Total Accepted:", total_accepted)
    print("Total Rejected:", total_rejected)

    context = {
        'jobs': jobs,
        'total_applications': total_applications,
        'total_pending': total_pending,
        'total_accepted': total_accepted,
        'total_rejected': total_rejected
    }

    return render(request, 'recruiter/JobHistory.html', context=context)


