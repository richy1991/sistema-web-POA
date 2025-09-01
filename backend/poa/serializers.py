from rest_framework import serializers
from .models import Poa, ObjetivoEspecifico, ActividadPoa, ActividadPoaResponsables, CronogramaPoa

class PoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poa
        fields = '__all__'

class ObjetivoEspecificoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjetivoEspecifico
        fields = '__all__'

class ActividadPoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActividadPoa
        fields = '__all__'

class ActividadPoaResponsablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActividadPoaResponsables
        fields = '__all__'

class CronogramaPoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CronogramaPoa
        fields = '__all__'
