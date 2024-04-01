from django.shortcuts import render, get_object_or_404

from job.models import Job, Application
from django.shortcuts import render
from django.http import JsonResponse


def c_list(request):
    apps = Application.objects.filter(status='request pending')
    return render(request, 'recruiter/ApplicationList.html', {'apps': apps})


def action(request):
    if request.method == 'POST':
        # Handle AJAX request for accepting or rejecting a candidate
        app_id = request.POST.get('id')
        status = request.POST.get('status')
        print(app_id, status)

        # Update status in the Application model
        try:
            application = Application.objects.get(id=app_id)
            application.status = status
            application.save()
            return JsonResponse({'success': True})
        except Application.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Application not found'})

    # If the request is not POST or not an AJAX request, render the template
    return render(request, 'recruiter/ApplicationList.html')


def accepted(request):
    application = Application.objects.filter(status='accepted')
    return render(request, 'recruiter/ApplicationList.html', {'application': application})


def rejected(request):
    application = Application.objects.filter(status='rejected')
    return render(request, 'recruiter/ApplicationList.html', {'aaps': application})


def candidate_applied_job(request):
    return render(request, 'recruiter/Application.html')
