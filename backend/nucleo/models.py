from django.db import models

class Carrera(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    creado_por = models.IntegerField(blank=True, null=True)
    modificado_por = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carrera'

    def __str__(self):
        return self.nombre

class ProgramaPoa(models.Model):
    id_programa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programa_poa'

    def __str__(self):
        return self.nombre

class EstadosActividad(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados_actividad'

    def __str__(self):
        return self.nombre

class TipoIndicador(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    formula = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_indicador'

    def __str__(self):
        return self.nombre

class PartidasPresupuestarias(models.Model):
    codigo_partida = models.CharField(primary_key=True, max_length=10)
    descripcion = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partidas_presupuestarias'

    def __str__(self):
        return f"{self.codigo_partida} - {self.descripcion}"

class Departamentos(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamentos'

    def __str__(self):
        return self.nombre
