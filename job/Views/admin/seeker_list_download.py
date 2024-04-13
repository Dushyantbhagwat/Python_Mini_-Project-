import csv

from django.http import HttpResponse
from django.views import View
from job.models import JobSeeker
from django.template.loader import get_template
# from xhtml2pdf import pisa

#
# class DownloadPDFView(View):
#     def get(self, request):
#         template_path = 'admin/job_seeker_list.html'
#         persons = JobSeeker.objects.all()
#
#         context = {
#             'persons': persons,
#         }
#
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="data.pdf"'
#
#         template = get_template(template_path)
#         html = template.render(context)
#
#         # Create PDF
#         # pisa_status = pisa.CreatePDF(html, dest=response)
#         # if pisa_status.err:
#         #     return HttpResponse('We had some errors <pre>' + html + '</pre>')
#         return response


class DownloadExcelView(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="JobSeeker.csv"'

        writer = csv.writer(response)
        writer.writerow(['Name', 'Gender', 'Contact', 'Email_Id', 'City'])

        for person in JobSeeker.objects.all():
            writer.writerow([person.full_name, person.gender, person.mobile_no, person.email_id, person.city])

        return response


class DownloadCSVView(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="JobSeeker.csv"'

        writer = csv.writer(response)
        writer.writerow(['Name', 'Gender', 'Contact', 'Email_Id', 'City'])

        for person in JobSeeker.objects.all():
            writer.writerow([person.name, person.age, person.country])

        return response


