from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=255)
    rol = models.CharField(max_length=20) # Consider using choices for this field in the future
    estado = models.BooleanField(default=True)
    ultimo_login = models.DateTimeField(blank=True, null=True)
    intentos_fallidos = models.IntegerField(default=0)
    bloqueado = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    creado_por = models.IntegerField(blank=True, null=True)
    modificado_por = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'

    def __str__(self):
        return self.nombre
