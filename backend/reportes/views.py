import pandas as pd
import io
from django.http import HttpResponse
from django.template.loader import render_to_string
from rest_framework.views import APIView
from weasyprint import HTML

from poa.models import Poa

class PoaExcelReportView(APIView):
    """
    Generates an Excel report of all POA records.
    """
    def get(self, request, *args, **kwargs):
        # Query the data
        poas = Poa.objects.all().select_related('id_carrera')

        # Prepare data for DataFrame
        data = {
            'ID': [poa.id_poa for poa in poas],
            'Gestión': [poa.gestion for poa in poas],
            'Carrera': [poa.id_carrera.nombre for poa in poas],
            'Unidad Solicitante': [poa.unidad_solicitante for poa in poas],
            'Estado': [poa.estado for poa in poas],
            'Fecha Creación': [poa.fecha_creacion for poa in poas],
        }

        df = pd.DataFrame(data)

        # Create an in-memory Excel file
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Reporte POA', index=False)

        output.seek(0)

        # Set up the HTTP response
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename="reporte_poa.xlsx"'

        return response

class PoaPdfReportView(APIView):
    """
    Generates a PDF report for a single POA record.
    """
    def get(self, request, poa_id, *args, **kwargs):
        try:
            poa = Poa.objects.select_related('id_carrera').get(id_poa=poa_id)
        except Poa.DoesNotExist:
            return HttpResponse("POA no encontrado", status=404)

        # Render HTML template with context
        context = {'poa': poa}
        html_string = render_to_string('reportes/poa_report.html', context)

        # Generate PDF
        pdf_file = HTML(string=html_string).write_pdf()

        # Set up the HTTP response
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="poa_{poa_id}_detalle.pdf"'

        return response
