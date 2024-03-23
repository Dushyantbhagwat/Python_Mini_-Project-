from django.urls import path
from . import views
from job.Views.job_seeker import sign_up, user_profile, user_update_profile
from job.Views.admin import *
from job.Views.recruiter import r_sign_up, r_profile, u_applied_list, recruiter_update_profile


urlpatterns = [
    path('', views.LandingPage.as_view(), name='landing_page'),
    path('login/', views.LoginView.as_view(), name='login'),

    # path('u1/', views.u1, name='u1'),
    path('j1/', views.job, name='j1'),

    path('u_signup/', sign_up.UserSignupView.as_view(), name='u_signup'),
    path('u_verify', sign_up.verify_otp_view, name='u_verify'),
    path('u_profile', user_profile.seeker_profile, name='u_profile'),
    path('u_update_profile', user_update_profile.UpdateProfileView.as_view(), name='u_update_profile'),
    path('u_landing_page', sign_up.u_landing_page, name='u_landing_page'),

    path('r_signup/', r_sign_up.RecruiterSignupView.as_view(), name='r_signup'),
    path('verify', r_sign_up.verify_otp_view, name='verify'),
    path('r_profile', r_profile.recruiter_profile, name='r_profile'),
    path('ap_list_r', u_applied_list.applied_seeker, name='ap_list_r'),
    path('r_landing_page', r_sign_up.u_landing_page, name='r_landing_page'),
    path('r_update_profile', recruiter_update_profile.UpdateProfile.as_view(), name='r_update_profile'),

]





