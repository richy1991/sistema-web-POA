from rest_framework import viewsets, status
from rest_framework.response import Response
import logging
from .models import Carrera, ProgramaPoa, EstadosActividad, TipoIndicador, PartidasPresupuestarias, Departamentos
from .serializers import (
    CarreraSerializer,
    ProgramaPoaSerializer,
    EstadosActividadSerializer,
    TipoIndicadorSerializer,
    PartidasPresupuestariasSerializer,
    DepartamentosSerializer
)

logger = logging.getLogger(__name__)

class CustomModelViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        try:
            logger.info(f"Creating a new {self.queryset.model.__name__} with data: {request.data}")
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            logger.info(f"{self.queryset.model.__name__} created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            logger.error(f"Error creating {self.queryset.model.__name__}: {e}", exc_info=True)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CarreraViewSet(CustomModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class ProgramaPoaViewSet(CustomModelViewSet):
    queryset = ProgramaPoa.objects.all()
    serializer_class = ProgramaPoaSerializer

class EstadosActividadViewSet(CustomModelViewSet):
    queryset = EstadosActividad.objects.all()
    serializer_class = EstadosActividadSerializer

class TipoIndicadorViewSet(CustomModelViewSet):
    queryset = TipoIndicador.objects.all()
    serializer_class = TipoIndicadorSerializer

class PartidasPresupuestariasViewSet(CustomModelViewSet):
    queryset = PartidasPresupuestarias.objects.all()
    serializer_class = PartidasPresupuestariasSerializer

class DepartamentosViewSet(CustomModelViewSet):
    queryset = Departamentos.objects.all()
    serializer_class = DepartamentosSerializer
