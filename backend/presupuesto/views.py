from rest_framework import viewsets
from .models import ItemsPoa, EjecucionPresupuestaria
from .serializers import ItemsPoaSerializer, EjecucionPresupuestariaSerializer
from nucleo.views import CustomModelViewSet

class ItemsPoaViewSet(CustomModelViewSet):
    queryset = ItemsPoa.objects.all()
    serializer_class = ItemsPoaSerializer

class EjecucionPresupuestariaViewSet(CustomModelViewSet):
    queryset = EjecucionPresupuestaria.objects.all()
    serializer_class = EjecucionPresupuestariaSerializer
