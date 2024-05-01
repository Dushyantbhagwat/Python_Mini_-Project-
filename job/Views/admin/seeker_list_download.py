import csv

from django.http import HttpResponse
from django.views import View
from job.models import JobSeeker
from django.template.loader import get_template

from django.http import FileResponse


##
# def venue_pdf(request):
#     buf = io.BytesIO()
#
#     c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
#
#     textob = c.beginText()
#     textob.setTextOrigin(inch, inch)
#     textob.setFont("Helvetica", 14)
#
#     lines = [
#         "This is line1",
#         "This is line2",
#         "This is line3"
#     ]
#
#     for line in lines:
#         textob.textLine(line)
#
#     c.drawText(textob)
#     c.showPage()
#     c.save()
#     buf.seek(0)
#
#     return FileResponse(buf, as_attachment=True, filename="venue.pdf")





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


# class DownloadPDFView(View):
#
#     @staticmethod
#     def get(request):
#         # Create a buffer to store the PDF data
#         buffer = BytesIO()
#
#         # Create a new PDF object
#         pdf = FPDF()
#         pdf.add_page()
#
#         # Define the data to be included in the PDF
#         data = [['Name', 'Gender', 'Contact', 'Email Id', 'City']]
#
#         # Fetch data from JobSeeker model
#         for person in JobSeeker.objects.all():
#             data.append([person.full_name, person.gender, person.mobile_no, person.email_id, person.city])
#
#         # Set font for the table
#         pdf.set_font("Arial", size=12)
#
#         # Add the table content
#         for row in data:
#             for item in row:
#                 pdf.cell(40, 10, txt=item, border=1)  # Adjust cell width and add border if needed
#             pdf.ln()  # Move to the next line after completing a row
#
#         # Write PDF content to the buffer
#         pdf_output = buffer.getvalue()
#         buffer.close()
#
#         # Create an HTTP response with PDF attachment
#         response = HttpResponse(pdf_output, content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="JobSeeker.pdf"'
#
#         return response




