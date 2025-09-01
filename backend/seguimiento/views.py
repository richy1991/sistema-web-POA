from rest_framework import viewsets
from .models import Seguimiento, Bitacora, BitacoraCambios
from .serializers import SeguimientoSerializer, BitacoraSerializer, BitacoraCambiosSerializer

class SeguimientoViewSet(viewsets.ModelViewSet):
    queryset = Seguimiento.objects.all()
    serializer_class = SeguimientoSerializer

class BitacoraViewSet(viewsets.ModelViewSet):
    queryset = Bitacora.objects.all()
    serializer_class = BitacoraSerializer

class BitacoraCambiosViewSet(viewsets.ModelViewSet):
    queryset = BitacoraCambios.objects.all()
    serializer_class = BitacoraCambiosSerializer
