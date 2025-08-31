from django.db import models

class SeguimientoActividad(models.Model):
    id = models.AutoField(primary_key=True)
    # actividad = models.ForeignKey('poa.Actividad', on_delete=models.CASCADE)
    descripcion_avance = models.TextField()
    fecha_reporte = models.DateField()

    class Meta:
        managed = False
        db_table = 'seguimiento_actividades'

class Evidencia(models.Model):
    id = models.AutoField(primary_key=True)
    # seguimiento = models.ForeignKey(SeguimientoActividad, on_delete=models.CASCADE)
    nombre_archivo = models.CharField(max_length=255)
    url_archivo = models.CharField(max_length=512) # Assuming URL to a file storage

    class Meta:
        managed = False
        db_table = 'evidencias'

    def __str__(self):
        return self.nombre_archivo
