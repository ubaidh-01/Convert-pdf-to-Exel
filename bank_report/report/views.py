from django.shortcuts import render
import tabula
import pandas as pd
import os
from django.http import HttpResponse

def convert_pdf_to_excel(request):
    if request.method == 'POST' and 'pdf_file' in request.FILES:
        pdf_file = request.FILES['pdf_file']

        # Convert PDF to Excel
        tables = tabula.read_pdf(pdf_file, pages='all', multiple_tables=True)
        df = pd.concat(tables)
        
        # Create a response with the Excel file
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="converted_excel.xlsx"'

        # Save the DataFrame as an Excel file and write it to the response
        df.to_excel(response, index=False)
        return response

    return render(request, 'index.html')
