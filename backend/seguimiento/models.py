from django.db import models
from cuentas.models import Usuario

class Seguimiento(models.Model):
    id_seguimiento = models.AutoField(primary_key=True)
    # This is a generic-like relation. We store the ID and the module name.
    # The actual object can be retrieved in the business logic layer.
    id_actividad = models.IntegerField()
    modulo = models.CharField(max_length=50)
    fecha_seguimiento = models.DateField()
    avance = models.TextField()
    observaciones = models.TextField(blank=True, null=True)
    usuario_registro = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='usuario_registro')

    class Meta:
        managed = False
        db_table = 'seguimiento'

    def __str__(self):
        return f"Seguimiento for {self.modulo} ID {self.id_actividad} on {self.fecha_seguimiento}"

class Bitacora(models.Model):
    id_log = models.AutoField(primary_key=True)
    modulo = models.CharField(max_length=50, blank=True, null=True)
    entidad = models.CharField(max_length=50, blank=True, null=True)
    operacion = models.CharField(max_length=20, blank=True, null=True)
    id_entidad_afectada = models.IntegerField(blank=True, null=True)
    usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='usuario', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitacora'

class BitacoraCambios(models.Model):
    id = models.AutoField(primary_key=True)
    tabla_afectada = models.CharField(max_length=50, blank=True, null=True)
    id_registro = models.IntegerField(blank=True, null=True)
    accion = models.CharField(max_length=20, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='usuario_id', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    detalle = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitacora_cambios'
