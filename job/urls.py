from django.urls import path
from . import views
from job.Views.job_seeker import sign_up, user_profile
from job.Views.admin import *
from job.Views.recruiter import r_sign_up


urlpatterns = [
    path('', views.LandingPage.as_view(), name='landing_page'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('u1/', views.u1, name='u1'),
    path('j1/', views.job, name='j1'),
    path('u_signup/', sign_up.UserSignupView.as_view(), name='u_signup'),
    path('r_signup/', r_sign_up.RecruiterSignupView.as_view(), name='r_signup'),
    path('u_profile/', user_profile.UserProfile.as_view(), name='u_profile'),
]

