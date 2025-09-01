import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poa_project.settings')
django.setup()

from poa.models import Poa, ObjetivoEspecifico, ActividadPoa
from nucleo.models import Carrera, ProgramaPoa
from cuentas.models import Usuario

# Clear existing data in the correct order to avoid foreign key constraint errors
ActividadPoa.objects.all().delete()
ObjetivoEspecifico.objects.all().delete()
Poa.objects.all().delete()
ProgramaPoa.objects.all().delete()
Carrera.objects.all().delete()
Usuario.objects.all().delete()

# Create a user
user, _ = Usuario.objects.get_or_create(
    id_usuario=1,
    defaults={
        'nombre': 'Test User',
        'correo': 'test@example.com',
        'contrasena': 'password', # In a real app, this should be a hash
        'rol': 'Docente'
    }
)

# Create a Carrera
carrera, _ = Carrera.objects.get_or_create(
    id_carrera=1,
    defaults={
        'nombre': 'Ingeniería de Software',
        'descripcion': 'Una carrera para formar ingenieros de software.'
    }
)

# Create a ProgramaPoa
programa, _ = ProgramaPoa.objects.get_or_create(
    id_programa=1,
    defaults={
        'nombre': 'Programa de Titulación',
        'descripcion': 'Un programa para ayudar a los estudiantes a titularse.'
    }
)

# Create a Poa
poa, _ = Poa.objects.get_or_create(
    id_poa=1,
    defaults={
        'id_carrera': carrera,
        'id_programa': programa,
        'gestion': 2024,
        'unidad_solicitante': 'Dirección de Carrera',
        'objetivo_institucional': 'Fortalecer la formación académica'
    }
)

# Create an ObjetivoEspecifico
objetivo, _ = ObjetivoEspecifico.objects.get_or_create(
    id_objetivo=1,
    defaults={
        'id_poa': poa,
        'codigo': 'OE-01',
        'descripcion': 'Mejorar el proceso de titulación.',
        'meta': 'Reducir el tiempo de titulación en un 20%'
    }
)

# Create an ActividadPoa
actividad, _ = ActividadPoa.objects.get_or_create(
    id_actividad=1,
    defaults={
        'id_objetivo': objetivo,
        'codigo': 'A-01',
        'nombre': 'Taller de tesis',
        'producto_esperado': 'Estudiantes con proyectos de tesis avanzados.',
        'fecha_inicio': '2024-01-01',
        'fecha_fin': '2024-06-30'
    }
)
actividad.responsables.add(user)

print("Database populated successfully.")
