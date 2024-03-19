from django.views import generic


class UserProfile(generic.TemplateView):
    template_name = 'job_seeker/UserProfile.html'
