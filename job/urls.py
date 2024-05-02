from django.urls import path
from . import views
from job.Views.job_seeker import sign_up, user_profile, user_update_profile, job_list, job_filtering
from job.Views.admin import seeker_list, recruiter_list, a_landing_page, seeker_list_download, recruiter_details
from job.Views.recruiter import (r_sign_up, r_profile, u_applied_list, recruiter_update_profile, post_jobs,
                                 candidate_list, job_history, applications_details)


urlpatterns = [
    path('', views.LandingPage.as_view(), name='landing_page'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('b_filter/', views.basic_filter, name='b_filter'),

    # path('u1/', views.u1, name='u1'),
    path('j1/', views.job, name='j1'),

    path('u_signup/', sign_up.UserSignupView.as_view(), name='u_signup'),
    path('u_verify/', sign_up.verify_otp_view_u, name='u_verify'),
    path('u_profile/', user_profile.seeker_profile, name='u_profile'),
    path('u_update_profile/', user_update_profile.UpdateProfileView.as_view(), name='u_update_profile'),
    path('u_landing_page/', sign_up.u_landing_page, name='u_landing_page'),
    path('job_list/', job_list.job_list, name='job_list'),
    path('job_details/<int:job_id>/', job_list.job_details, name='job_details'),
    path('apply/', job_list.apply, name='apply'),
    path('filter-jobs/', job_filtering.filter_jobs, name='filter_jobs'),
    path('job_status/', job_list.job_status, name='job_status'),
    path('accepted_jobs', job_list.job_accepted, name='accepted_jobs'),
    path('rejected_jobs', job_list.job_rejected, name='rejected_jobs'),
    # path('basic_filtering/', sign_up.u_landing_filter, name='basic_filtering'),
    path('resume', applications_details.search_resumes, name='resume'),

    # path('u_filter_landing/', job_filtering.LandingFilter.as_view(), name='u_filter_landing'),
    # path('job_filter/', job_filtering.filter_job, name='job_filter'),
    # path('all_job_filter/', job_filtering.all_filter_job, name='all_job_filter'),


    path('r_signup/', r_sign_up.RecruiterSignupView.as_view(), name='r_signup'),
    path('verify/', r_sign_up.verify_otp_view, name='verify'),
    path('r_profile/', r_profile.recruiter_profile, name='r_profile'),
    # path('ap_list_r/', u_applied_list.applied_seeker, name='ap_list_r'),
    path('r_landing_page/', r_sign_up.u_landing_page, name='r_landing_page'),
    path('r_update_profile/', recruiter_update_profile.UpdateProfile.as_view(), name='r_update_profile'),
    path('post_jobs/', post_jobs.post_jobs, name='post_jobs'),

    path('job_history/', job_history.jobs_history, name='job_history'),
    path('candidate_list/<int:job_id>/', candidate_list.candidate_applied, name='candidate_list'),
    path('pending_candidate_list/<int:job_id>/', candidate_list.pending_candidate_list, name='pending_candidate_list'),
    path('accepted_candidate_list/<int:job_id>/', candidate_list.accepted_candidate_list, name='accepted_candidate_list'),
    path('rejected_candidate_list/<int:job_id>/', candidate_list.rejected_candidate_list, name='rejected_candidate_list'),
    path('applications/<int:app_id>/', applications_details.application, name='applications'),
    path('action/', candidate_list.action, name='action'),





    path('admin_landing_page/', a_landing_page.ALandingPage.as_view(), name='admin_landing_page'),
    path('seeker_list_admin/', seeker_list.registered_seeker_list, name='seeker_list_admin'),
    path('recruiter_list/', recruiter_list.recruiter_list, name='recruiter_list'),


    path('recruiter_profile/<int:recruiter_id>/', recruiter_details.recruiter_profile, name='recruiter_profile'),

    path('recruiter_status_update', recruiter_details.update_status, name='recruiter_status_update'),

    path('accepted_recruiter_list/', recruiter_list.accepted_recruiter_list, name='accepted_recruiter_list'),
    path('rejected_recruiter_list/', recruiter_list.rejected_recruiter_list, name='rejected_recruiter_list'),
    path('delete_job_seeker/<int:user_id>/', seeker_list.delete_job_seeker, name='delete_job_seeker'),
    path('seeker_list_excel/', seeker_list_download.DownloadExcelView.as_view(), name='seeker_list_excel'),
    # path('seeker_list_pdf/', seeker_list_download.venue_pdf, name='seeker_list_pdf'),

]
