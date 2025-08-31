from django.db import models

class ItemPresupuestario(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=255)
    presupuesto_asignado = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'items_presupuestarios'

    def __str__(self):
        return f'{self.codigo} - {self.descripcion}'
