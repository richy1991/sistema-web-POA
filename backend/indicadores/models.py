from django.db import models
from poa.models import ActividadPoa
from nucleo.models import TipoIndicador

class Indicadores(models.Model):
    id_indicador = models.AutoField(primary_key=True)
    id_actividad = models.ForeignKey(ActividadPoa, models.DO_NOTHING, db_column='id_actividad')
    nombre = models.CharField(max_length=200)
    tipo_id = models.ForeignKey(TipoIndicador, models.DO_NOTHING, db_column='tipo_id', blank=True, null=True)
    formula = models.CharField(max_length=500, blank=True, null=True)
    frecuencia = models.CharField(max_length=50, blank=True, null=True)
    fuente_dato = models.CharField(max_length=200, blank=True, null=True)
    linea_base = models.CharField(max_length=100, blank=True, null=True)
    meta = models.CharField(max_length=100, blank=True, null=True)
    unidad_medida = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicadores'
        verbose_name = 'Indicador'
        verbose_name_plural = 'Indicadores'

    def __str__(self):
        return self.nombre
