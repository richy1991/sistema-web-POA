from rest_framework import viewsets
from .models import Indicadores
from .serializers import IndicadoresSerializer
from nucleo.views import CustomModelViewSet

class IndicadoresViewSet(CustomModelViewSet):
    queryset = Indicadores.objects.all()
    serializer_class = IndicadoresSerializer
