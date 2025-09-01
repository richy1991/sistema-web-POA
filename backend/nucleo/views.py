from rest_framework import viewsets
from .models import Carrera, ProgramaPoa, EstadosActividad, TipoIndicador, PartidasPresupuestarias, Departamentos
from .serializers import (
    CarreraSerializer,
    ProgramaPoaSerializer,
    EstadosActividadSerializer,
    TipoIndicadorSerializer,
    PartidasPresupuestariasSerializer,
    DepartamentosSerializer
)

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class ProgramaPoaViewSet(viewsets.ModelViewSet):
    queryset = ProgramaPoa.objects.all()
    serializer_class = ProgramaPoaSerializer

class EstadosActividadViewSet(viewsets.ModelViewSet):
    queryset = EstadosActividad.objects.all()
    serializer_class = EstadosActividadSerializer

class TipoIndicadorViewSet(viewsets.ModelViewSet):
    queryset = TipoIndicador.objects.all()
    serializer_class = TipoIndicadorSerializer

class PartidasPresupuestariasViewSet(viewsets.ModelViewSet):
    queryset = PartidasPresupuestarias.objects.all()
    serializer_class = PartidasPresupuestariasSerializer

class DepartamentosViewSet(viewsets.ModelViewSet):
    queryset = Departamentos.objects.all()
    serializer_class = DepartamentosSerializer
