from django.db import models

class PlanOperativo(models.Model):
    id = models.AutoField(primary_key=True)
    # Assuming foreign keys to models in other apps
    # Note: Use the actual model name for ForeignKey, not the db_table name
    # carrera = models.ForeignKey('core.Carrera', on_delete=models.CASCADE, db_column='carrera_id')
    # periodo = models.ForeignKey('core.PeriodoAcademico', on_delete=models.CASCADE, db_column='periodo_id')
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'planes_operativos'

    def __str__(self):
        return f'POA {self.id}'
