from django.db import models

# This is an example of how to map a model to an existing database table.
# Django will not create, modify, or delete this table.
# You need to define fields that match your existing table columns.

class Usuario(models.Model):
    # Assuming you have at least these fields in your 'usuarios' table
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'usuarios'  # The exact name of your existing table in PostgreSQL

    def __str__(self):
        return self.username
