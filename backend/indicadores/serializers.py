from rest_framework import serializers
from .models import Indicadores
from poa.models import ActividadPoa
from nucleo.models import TipoIndicador

class IndicadoresSerializer(serializers.ModelSerializer):
    id_actividad = serializers.PrimaryKeyRelatedField(queryset=ActividadPoa.objects.all(), required=True)
    tipo_id = serializers.PrimaryKeyRelatedField(queryset=TipoIndicador.objects.all(), required=False)

    class Meta:
        model = Indicadores
        fields = [
            'id_indicador', 'id_actividad', 'nombre', 'tipo_id', 'formula',
            'frecuencia', 'fuente_dato', 'linea_base', 'meta', 'unidad_medida'
        ]
        read_only_fields = ['id_indicador']
