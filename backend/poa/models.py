from django.db import models

class PlanOperativo(models.Model):
    id = models.AutoField(primary_key=True)
    # Ejemplo de ForeignKey a un modelo en otra app:
    # carrera = models.ForeignKey('nucleo.Carrera', on_delete=models.CASCADE, db_column='carrera_id')
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'planes_operativos'

    def __str__(self):
        return f'POA {self.id}'
