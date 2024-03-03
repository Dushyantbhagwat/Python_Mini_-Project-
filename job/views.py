from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import generic, View
from .models import JobSeeker
from .utils import *
from django.contrib import messages
from django.core.exceptions import ValidationError


# Create your Views here.

class LandingPage(generic.TemplateView):
    template_name = 'landing_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve data from the database
        options = JobSeeker.objects.values_list('location', flat=True).distinct()
        context['options'] = options
        return context


def login(request):
    return render(request, 'login.html')


def u1(request):
    return render(request, 'u1.html')


def job(request):
    return render(request, 'j1.html')


