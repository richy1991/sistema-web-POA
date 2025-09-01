from rest_framework import serializers
from .models import Poa, ObjetivoEspecifico, ActividadPoa, ActividadPoaResponsables, CronogramaPoa
from nucleo.models import Carrera, ProgramaPoa, EstadosActividad
from cuentas.models import Usuario

class PoaSerializer(serializers.ModelSerializer):
    id_carrera = serializers.IntegerField()
    id_programa = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Poa
        fields = [
            'id_poa', 'id_carrera', 'id_programa', 'gestion', 'unidad_solicitante',
            'objetivo_institucional', 'estado', 'fecha_creacion'
        ]
        read_only_fields = ['id_poa', 'fecha_creacion']

    def create(self, validated_data):
        carrera_id = validated_data.pop('id_carrera')
        programa_id = validated_data.pop('id_programa', None)

        try:
            carrera = Carrera.objects.get(id_carrera=carrera_id)
        except Carrera.DoesNotExist:
            raise serializers.ValidationError(f"Carrera with id {carrera_id} does not exist.")

        programa = None
        if programa_id:
            try:
                programa = ProgramaPoa.objects.get(id_programa=programa_id)
            except ProgramaPoa.DoesNotExist:
                raise serializers.ValidationError(f"ProgramaPoa with id {programa_id} does not exist.")

        poa = Poa.objects.create(id_carrera=carrera, id_programa=programa, **validated_data)
        return poa

class ObjetivoEspecificoSerializer(serializers.ModelSerializer):
    id_poa = serializers.PrimaryKeyRelatedField(queryset=Poa.objects.all(), required=True)

    class Meta:
        model = ObjetivoEspecifico
        fields = ['id_objetivo', 'id_poa', 'codigo', 'descripcion', 'meta', 'linea_base']
        read_only_fields = ['id_objetivo']

class ActividadPoaSerializer(serializers.ModelSerializer):
    id_objetivo = serializers.PrimaryKeyRelatedField(queryset=ObjetivoEspecifico.objects.all(), required=True)
    id_estado = serializers.PrimaryKeyRelatedField(queryset=EstadosActividad.objects.all(), required=False)
    responsables = serializers.PrimaryKeyRelatedField(many=True, queryset=Usuario.objects.all())

    class Meta:
        model = ActividadPoa
        fields = [
            'id_actividad', 'id_objetivo', 'codigo', 'nombre', 'producto_esperado',
            'fecha_inicio', 'fecha_fin', 'id_estado', 'avance_fisico', 'avance_financiero',
            'anio', 'fecha_creacion', 'fecha_modificacion', 'creado_por', 'modificado_por',
            'responsables'
        ]
        read_only_fields = ['id_actividad', 'fecha_creacion', 'fecha_modificacion']

class ActividadPoaResponsablesSerializer(serializers.ModelSerializer):
    id_actividad = serializers.PrimaryKeyRelatedField(queryset=ActividadPoa.objects.all(), required=True)
    id_usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), required=True)

    class Meta:
        model = ActividadPoaResponsables
        fields = ['id_actividad', 'id_usuario']

class CronogramaPoaSerializer(serializers.ModelSerializer):
    id_actividad = serializers.PrimaryKeyRelatedField(queryset=ActividadPoa.objects.all(), required=True)

    class Meta:
        model = CronogramaPoa
        fields = ['id_cronograma', 'id_actividad', 'mes', 'ejecutado']
        read_only_fields = ['id_cronograma']
