from django.db import models
from poa.models import ActividadPoa
from nucleo.models import PartidasPresupuestarias

class ItemsPoa(models.Model):
    id_item = models.AutoField(primary_key=True)
    id_actividad = models.ForeignKey(ActividadPoa, models.DO_NOTHING, db_column='id_actividad')
    descripcion = models.CharField(max_length=300)
    unidad = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    costo_unitario = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    # The 'subtotal' field is a generated column in PostgreSQL.
    # We include it in the model for reading purposes but make it not editable.
    subtotal = models.DecimalField(max_digits=18, decimal_places=2, editable=False, blank=True, null=True)
    fuente_financiamiento = models.CharField(max_length=100, blank=True, null=True)
    codigo_partida = models.ForeignKey(PartidasPresupuestarias, models.DO_NOTHING, db_column='codigo_partida', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items_poa'

    def __str__(self):
        return self.descripcion

class EjecucionPresupuestaria(models.Model):
    id = models.AutoField(primary_key=True)
    id_item = models.ForeignKey(ItemsPoa, models.DO_NOTHING, db_column='id_item')
    fecha = models.DateField()
    monto_ejecutado = models.DecimalField(max_digits=18, decimal_places=2)
    descripcion = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ejecucion_presupuestaria'

    def __str__(self):
        return f"Ejecución de {self.id_item.descripcion} por {self.monto_ejecutado}"
