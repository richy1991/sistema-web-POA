from rest_framework import serializers
from .models import Seguimiento, Bitacora, BitacoraCambios

class SeguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguimiento
        fields = '__all__'

class BitacoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bitacora
        fields = '__all__'

class BitacoraCambiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitacoraCambios
        fields = '__all__'
