from django.shortcuts import render, redirect
import json
from django.contrib.auth.decorators import login_required
from job.models import Recruiter
from django.http import JsonResponse


def recruiter_list(request):
    recruiters = Recruiter.objects.filter(status='request pending')
    return render(request, 'admin/recruiter_list.html', {'recruiters': recruiters})


def accepted_recruiter_list(request):
    recruiters = Recruiter.objects.filter(status='Accepted')
    return render(request, 'admin/recruiter_list.html', {'recruiters': recruiters})


def rejected_recruiter_list(request):
    recruiters = Recruiter.objects.filter(status='Rejected')
    return render(request, 'admin/recruiter_list.html', {'recruiters': recruiters})


# def accepted_recruiter_list(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         selected_value = data.get('selected_value')
#         print("Selected value received:", selected_value)
#         # Process the selected value as needed
#         if selected_value == 'accepted':
#             recruiters = Recruiter.objects.filter(status='Accepted')
#             return render(request, 'admin/recruiter_list.html', {'recruiters': recruiters})
#         elif selected_value == 'rejected':
#             recruiters = Recruiter.objects.filter(status='Rejected')
#             return render(request, 'admin/recruiter_list.html', {'recruiters': recruiters})
#
#         return JsonResponse({'message': 'Value received successfully'})
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=405)
