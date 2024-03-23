from django.shortcuts import render


def applied_seeker(request):
    return render(request, 'recruiter/ApplicationList.html')
