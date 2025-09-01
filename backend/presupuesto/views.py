from rest_framework import viewsets
from .models import ItemsPoa, EjecucionPresupuestaria
from .serializers import ItemsPoaSerializer, EjecucionPresupuestariaSerializer

class ItemsPoaViewSet(viewsets.ModelViewSet):
    queryset = ItemsPoa.objects.all()
    serializer_class = ItemsPoaSerializer

class EjecucionPresupuestariaViewSet(viewsets.ModelViewSet):
    queryset = EjecucionPresupuestaria.objects.all()
    serializer_class = EjecucionPresupuestariaSerializer
