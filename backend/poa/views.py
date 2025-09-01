from rest_framework import viewsets
from .models import Poa, ObjetivoEspecifico, ActividadPoa, ActividadPoaResponsables, CronogramaPoa
from .serializers import (
    PoaSerializer,
    ObjetivoEspecificoSerializer,
    ActividadPoaSerializer,
    ActividadPoaResponsablesSerializer,
    CronogramaPoaSerializer,
)

class PoaViewSet(viewsets.ModelViewSet):
    queryset = Poa.objects.all()
    serializer_class = PoaSerializer

class ObjetivoEspecificoViewSet(viewsets.ModelViewSet):
    queryset = ObjetivoEspecifico.objects.all()
    serializer_class = ObjetivoEspecificoSerializer

class ActividadPoaViewSet(viewsets.ModelViewSet):
    queryset = ActividadPoa.objects.all()
    serializer_class = ActividadPoaSerializer

class ActividadPoaResponsablesViewSet(viewsets.ModelViewSet):
    queryset = ActividadPoaResponsables.objects.all()
    serializer_class = ActividadPoaResponsablesSerializer

class CronogramaPoaViewSet(viewsets.ModelViewSet):
    queryset = CronogramaPoa.objects.all()
    serializer_class = CronogramaPoaSerializer
