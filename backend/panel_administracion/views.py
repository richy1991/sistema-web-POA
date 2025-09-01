from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count, Q

from poa.models import Poa, ActividadPoa
from indicadores.models import Indicadores

class KpiView(APIView):
    """
    Endpoint to retrieve Key Performance Indicators (KPIs) for the admin panel.
    Filters statistics by a 'gestion' (year) query parameter.
    """
    def get(self, request, *args, **kwargs):
        # Get 'gestion' parameter from URL, return error if not present
        gestion = request.query_params.get('gestion', None)
        if not gestion:
            return Response(
                {"error": "El parámetro 'gestion' es requerido."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            gestion = int(gestion)
        except ValueError:
            return Response(
                {"error": "El parámetro 'gestion' debe ser un año válido."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 1. Total de POAs registrados en la gestión
        total_poa = Poa.objects.filter(gestion=gestion).count()

        # 2. Actividades planificadas vs. ejecutadas
        # QuerySet base para actividades de la gestión
        actividades_qs = ActividadPoa.objects.filter(id_objetivo__id_poa__gestion=gestion)

        actividades_planificadas = actividades_qs.count()
        actividades_ejecutadas = actividades_qs.filter(avance_fisico__gte=100).count()

        # 3. Indicadores cumplidos (asumiendo que es por actividad completada)
        indicadores_cumplidos = Indicadores.objects.filter(
            id_actividad__id_objetivo__id_poa__gestion=gestion,
            id_actividad__avance_fisico__gte=100
        ).count()

        # Construct the response JSON
        data = {
            "total_poa": total_poa,
            "actividades_planificadas": actividades_planificadas,
            "actividades_ejecutadas": actividades_ejecutadas,
            "indicadores_cumplidos": indicadores_cumplidos
        }

        return Response(data, status=status.HTTP_200_OK)
