from django.db import models

# Note: We are importing models from other apps to define relationships.
# This is standard practice in Django for modular architectures.
from nucleo.models import Carrera, ProgramaPoa, EstadosActividad
from cuentas.models import Usuario

class Poa(models.Model):
    id_poa = models.AutoField(primary_key=True)
    id_carrera = models.ForeignKey(Carrera, models.DO_NOTHING, db_column='id_carrera')
    id_programa = models.ForeignKey(ProgramaPoa, models.DO_NOTHING, db_column='id_programa', blank=True, null=True)
    gestion = models.IntegerField()
    unidad_solicitante = models.CharField(max_length=200)
    objetivo_institucional = models.CharField(max_length=2000)
    estado = models.CharField(max_length=30, default='Borrador')
    fecha_creacion = models.DateField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'poa'

    def __str__(self):
        return f"POA {self.id_poa} - {self.gestion}"

class ObjetivoEspecifico(models.Model):
    id_objetivo = models.AutoField(primary_key=True)
    id_poa = models.ForeignKey(Poa, models.DO_NOTHING, db_column='id_poa')
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=1000)
    meta = models.CharField(max_length=200, blank=True, null=True)
    linea_base = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objetivo_especifico'

    def __str__(self):
        return self.codigo

class ActividadPoa(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    id_objetivo = models.ForeignKey(ObjetivoEspecifico, models.DO_NOTHING, db_column='id_objetivo')
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=500)
    producto_esperado = models.CharField(max_length=500)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    id_estado = models.ForeignKey(EstadosActividad, models.DO_NOTHING, db_column='id_estado', blank=True, null=True)
    avance_fisico = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    avance_financiero = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    creado_por = models.IntegerField(blank=True, null=True)
    modificado_por = models.IntegerField(blank=True, null=True)
    responsables = models.ManyToManyField(Usuario, through='ActividadPoaResponsables')

    class Meta:
        managed = False
        db_table = 'actividad_poa'

    def __str__(self):
        return self.nombre

class ActividadPoaResponsables(models.Model):
    id_actividad = models.OneToOneField(ActividadPoa, models.DO_NOTHING, db_column='id_actividad', primary_key=True)
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'actividad_poa_responsables'
        unique_together = (('id_actividad', 'id_usuario'),)

class CronogramaPoa(models.Model):
    id_cronograma = models.AutoField(primary_key=True)
    id_actividad = models.ForeignKey(ActividadPoa, models.DO_NOTHING, db_column='id_actividad')
    mes = models.IntegerField()
    ejecutado = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'cronograma_poa'

    def __str__(self):
        return f"Cronograma para Actividad {self.id_actividad_id} - Mes {self.mes}"
