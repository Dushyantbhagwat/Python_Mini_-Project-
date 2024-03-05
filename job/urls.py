from django.urls import path
from . import views
from job.Views.job_seeker import sign_up
from job.Views.admin import *
from job.Views.recruiter import *


urlpatterns = [
    path('', views.LandingPage.as_view(), name='landing_page'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('u1/', views.u1, name='u1'),
    path('j1/', views.job, name='j1'),
    path('u_signup/', sign_up.UserSignupView.as_view(), name='u_signup'),

]
