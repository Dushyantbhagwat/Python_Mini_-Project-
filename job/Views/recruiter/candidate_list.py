from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from job.models import Job, Application
from django.shortcuts import render
from django.http import JsonResponse


def action(request):
    if request.method == 'POST':
        # Handle AJAX request for accepting or rejecting a candidate
        app_id = request.POST.get('id')
        status = request.POST.get('status')
        reason = request.POST.get('reason')
        print(app_id, status, reason)

        # Update status in the Application model
        try:
            application = Application.objects.get(id=app_id)
            application.status = status
            application.reason = reason
            application.save()
            return JsonResponse({'success': True})
        except Application.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Application not found'})

    # If the request is not POST or not an AJAX request, render the template
    return render(request, 'recruiter/ApplicationList.html')


def candidate_applied(request, job_id):
    apps = Application.objects.filter(job_id=job_id)
    print(apps)
    return render(request, 'recruiter/ApplicationList.html', {'apps': apps, 'job_id': job_id})


def pending_candidate_list(request, job_id):
    apps = Application.objects.filter(job_id=job_id, status='Pending')
    return render(request, 'recruiter/ApplicationList.html', {'apps': apps, 'job_id': job_id})


def accepted_candidate_list(request, job_id):
    apps = Application.objects.filter(job_id=job_id, status='Accepted')
    return render(request, 'recruiter/ApplicationList.html', {'apps': apps, 'job_id': job_id})


def rejected_candidate_list(request, job_id):
    apps = Application.objects.filter(job_id=job_id, status='Rejected')
    return render(request, 'recruiter/ApplicationList.html', {'apps': apps, 'job_id': job_id})










# def c_list(request):
#     selected_job_id = request.session.get('selectedJobId')
#     print("Selected Job ID from session:", selected_job_id)
#     if selected_job_id:
#         job = Job.objects.filter(id=selected_job_id).first()
#         if job:
#             apps = job.application_set.filter(status='Pending')
#             return render(request, 'recruiter/ApplicationList.html', {'apps': apps})
#         else:
#             messages.error(request, 'Job not found!')
#     else:
#         messages.error(request, 'No job selected!')
#     return render(request, 'recruiter/ApplicationList.html', {})

