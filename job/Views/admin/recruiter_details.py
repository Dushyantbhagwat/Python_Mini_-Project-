import json

from django.contrib import messages
from django.shortcuts import render
from job.models import Recruiter
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


def recruiter_profile(request, recruiter_id):
    recruiter = get_object_or_404(Recruiter, id=recruiter_id)
    return render(request, 'admin/recruiter_details.html', {'recruiter': recruiter})


def update_status(request):
    global message
    if request.method == 'POST':
        status = request.POST.get('status')
        recruiter_id = request.POST.get('recruiter_id')
        try:
            recruiter = Recruiter.objects.get(id=recruiter_id)
            if status == 'accepted':
                recruiter.status = 'Accepted'
                message = "Recruiter is Accepted!"
            elif status == 'rejected':
                recruiter.status = 'Rejected'
                message = "Recruiter is rejected!"
            recruiter.save()
            messages.success(request, message=message)
            return HttpResponseRedirect('/recruiter_list/')  # Redirect to a success page or appropriate URL
        except Recruiter.DoesNotExist:
            return render(request, 'admin/recruiter_details.html', {'message': 'Recruiter not found'}, status=404)
    else:
        return render(request, 'admin/recruiter_details.html', {'message': 'Invalid request method'}, status=405)
