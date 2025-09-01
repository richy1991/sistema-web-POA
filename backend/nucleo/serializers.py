from rest_framework import serializers
from .models import Carrera, ProgramaPoa, EstadosActividad, TipoIndicador, PartidasPresupuestarias, Departamentos

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = ['id_carrera', 'nombre', 'descripcion', 'fecha_creacion', 'fecha_modificacion', 'creado_por', 'modificado_por']
        read_only_fields = ['id_carrera', 'fecha_creacion', 'fecha_modificacion']

    def validate_nombre(self, value):
        if Carrera.objects.filter(nombre=value).exists():
            raise serializers.ValidationError("Ya existe una carrera con este nombre.")
        return value

class ProgramaPoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaPoa
        fields = ['id_programa', 'nombre', 'descripcion']
        read_only_fields = ['id_programa']

class EstadosActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadosActividad
        fields = ['id_estado', 'nombre', 'descripcion', 'color']
        read_only_fields = ['id_estado']

class TipoIndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIndicador
        fields = ['id_tipo', 'nombre', 'descripcion', 'formula']
        read_only_fields = ['id_tipo']

class PartidasPresupuestariasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartidasPresupuestarias
        fields = ['codigo_partida', 'descripcion']

class DepartamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamentos
        fields = ['id_departamento', 'nombre', 'descripcion']
        read_only_fields = ['id_departamento']
