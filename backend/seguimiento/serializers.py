from rest_framework import serializers
from .models import Seguimiento, Bitacora, BitacoraCambios
from cuentas.models import Usuario

class SeguimientoSerializer(serializers.ModelSerializer):
    usuario_registro = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), required=True)

    class Meta:
        model = Seguimiento
        fields = [
            'id_seguimiento', 'id_actividad', 'modulo', 'fecha_seguimiento',
            'avance', 'observaciones', 'usuario_registro'
        ]
        read_only_fields = ['id_seguimiento']

class BitacoraSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), required=False)

    class Meta:
        model = Bitacora
        fields = [
            'id_log', 'modulo', 'entidad', 'operacion', 'id_entidad_afectada',
            'usuario', 'fecha', 'descripcion'
        ]
        read_only_fields = ['id_log', 'fecha']

class BitacoraCambiosSerializer(serializers.ModelSerializer):
    usuario_id = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), required=False)

    class Meta:
        model = BitacoraCambios
        fields = ['id', 'tabla_afectada', 'id_registro', 'accion', 'usuario_id', 'fecha', 'detalle']
        read_only_fields = ['id', 'fecha']
