import csv

from django.http import HttpResponse
from django.views import View
from job.models import JobSeeker
from django.template.loader import get_template
# from xhtml2pdf import pisa
from fpdf import FPDF
from io import BytesIO


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


class DownloadPDFView(View):

    def get(self, request):

        # Create a buffer to store the PDF data
        buffer = BytesIO()

        # Create a new PDF object
        pdf = FPDF()
        pdf.add_page()

        # Define the data to be included in the PDF
        data = [['Name', 'Gender', 'Contact', 'Email Id', 'City']]

        # Fetch data from JobSeeker model
        for person in JobSeeker.objects.all():
            data.append([person.full_name, person.gender, person.mobile_no, person.email_id, person.city])

        # Set font for the table
        pdf.set_font("Arial", size=12)

        # Add the table header
        for row in data:
            for item in row:
                pdf.cell(40, 10, txt=item, ln=True)

        # Write the PDF to the buffer
        pdf_output = buffer.getvalue()
        buffer.close()

        # Create an HTTP response with PDF attachment
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="JobSeeker.pdf"'
        response.write(pdf_output)

        return response