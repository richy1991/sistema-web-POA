from django.db import models

class Carrera(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=50, unique=True)

    class Meta:
        managed = False
        db_table = 'carreras'

    def __str__(self):
        return self.nombre

class PeriodoAcademico(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100) # e.g., '2024-2025'
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        managed = False
        db_table = 'periodos_academicos'

    def __str__(self):
        return self.nombre
