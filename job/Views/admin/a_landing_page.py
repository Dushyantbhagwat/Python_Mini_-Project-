from django.views import generic


class ALandingPage(generic.TemplateView):

    template_name = 'admin/AdminLandingPage.html'
