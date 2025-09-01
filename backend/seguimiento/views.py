from rest_framework import viewsets
from .models import Seguimiento, Bitacora, BitacoraCambios
from .serializers import SeguimientoSerializer, BitacoraSerializer, BitacoraCambiosSerializer
from nucleo.views import CustomModelViewSet

class SeguimientoViewSet(CustomModelViewSet):
    queryset = Seguimiento.objects.all()
    serializer_class = SeguimientoSerializer

class BitacoraViewSet(CustomModelViewSet):
    queryset = Bitacora.objects.all()
    serializer_class = BitacoraSerializer

class BitacoraCambiosViewSet(CustomModelViewSet):
    queryset = BitacoraCambios.objects.all()
    serializer_class = BitacoraCambiosSerializer
