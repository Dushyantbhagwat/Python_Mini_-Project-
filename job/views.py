from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

# Create your views here.


class LandingPage(generic.TemplateView):
    template_name = 'landing_page.html'


def login(request):
    return render(request, 'login.html')


def u1(request):
    return render(request, 'u1.html')


def job(request):
    return render(request, 'j1.html')
