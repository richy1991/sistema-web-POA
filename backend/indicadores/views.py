from rest_framework import viewsets
from .models import Indicadores
from .serializers import IndicadoresSerializer

class IndicadoresViewSet(viewsets.ModelViewSet):
    queryset = Indicadores.objects.all()
    serializer_class = IndicadoresSerializer
