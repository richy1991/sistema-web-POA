from rest_framework import serializers
from .models import Carrera, ProgramaPoa, EstadosActividad, TipoIndicador, PartidasPresupuestarias, Departamentos

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

class ProgramaPoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaPoa
        fields = '__all__'

class EstadosActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadosActividad
        fields = '__all__'

class TipoIndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIndicador
        fields = '__all__'

class PartidasPresupuestariasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartidasPresupuestarias
        fields = '__all__'

class DepartamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamentos
        fields = '__all__'
