from rest_framework import viewsets
from .models import Poa, ObjetivoEspecifico, ActividadPoa, ActividadPoaResponsables, CronogramaPoa
from .serializers import (
    PoaSerializer,
    ObjetivoEspecificoSerializer,
    ActividadPoaSerializer,
    ActividadPoaResponsablesSerializer,
    CronogramaPoaSerializer,
)
from nucleo.views import CustomModelViewSet

class PoaViewSet(CustomModelViewSet):
    queryset = Poa.objects.all()
    serializer_class = PoaSerializer

class ObjetivoEspecificoViewSet(CustomModelViewSet):
    queryset = ObjetivoEspecifico.objects.all()
    serializer_class = ObjetivoEspecificoSerializer

class ActividadPoaViewSet(CustomModelViewSet):
    queryset = ActividadPoa.objects.all()
    serializer_class = ActividadPoaSerializer

class ActividadPoaResponsablesViewSet(CustomModelViewSet):
    queryset = ActividadPoaResponsables.objects.all()
    serializer_class = ActividadPoaResponsablesSerializer

class CronogramaPoaViewSet(CustomModelViewSet):
    queryset = CronogramaPoa.objects.all()
    serializer_class = CronogramaPoaSerializer
