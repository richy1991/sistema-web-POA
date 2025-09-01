from rest_framework import serializers
from .models import Indicadores

class IndicadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicadores
        fields = '__all__'
