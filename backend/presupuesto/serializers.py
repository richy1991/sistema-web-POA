from rest_framework import serializers
from .models import ItemsPoa, EjecucionPresupuestaria

class ItemsPoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsPoa
        fields = '__all__'

class EjecucionPresupuestariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EjecucionPresupuestaria
        fields = '__all__'
