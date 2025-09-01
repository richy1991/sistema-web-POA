from rest_framework import serializers
from .models import ItemsPoa, EjecucionPresupuestaria
from poa.models import ActividadPoa
from nucleo.models import PartidasPresupuestarias

class ItemsPoaSerializer(serializers.ModelSerializer):
    id_actividad = serializers.PrimaryKeyRelatedField(queryset=ActividadPoa.objects.all(), required=True)
    codigo_partida = serializers.PrimaryKeyRelatedField(queryset=PartidasPresupuestarias.objects.all(), required=False)

    class Meta:
        model = ItemsPoa
        fields = [
            'id_item', 'id_actividad', 'descripcion', 'unidad', 'cantidad',
            'costo_unitario', 'subtotal', 'fuente_financiamiento', 'codigo_partida'
        ]
        read_only_fields = ['id_item', 'subtotal']

    def create(self, validated_data):
        # The subtotal is calculated in the model, so we don't need to do it here.
        # However, if the logic was not in the model, we would calculate it here.
        # For example:
        # validated_data['subtotal'] = validated_data['cantidad'] * validated_data['costo_unitario']
        return super().create(validated_data)

class EjecucionPresupuestariaSerializer(serializers.ModelSerializer):
    id_item = serializers.PrimaryKeyRelatedField(queryset=ItemsPoa.objects.all(), required=True)

    class Meta:
        model = EjecucionPresupuestaria
        fields = ['id', 'id_item', 'fecha', 'monto_ejecutado', 'descripcion']
        read_only_fields = ['id']
