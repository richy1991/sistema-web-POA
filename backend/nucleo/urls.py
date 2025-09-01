from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CarreraViewSet,
    ProgramaPoaViewSet,
    EstadosActividadViewSet,
    TipoIndicadorViewSet,
    PartidasPresupuestariasViewSet,
    DepartamentosViewSet
)

router = DefaultRouter()
router.register(r'carreras', CarreraViewSet, basename='carrera')
router.register(r'programas-poa', ProgramaPoaViewSet, basename='programapoa')
router.register(r'estados-actividad', EstadosActividadViewSet, basename='estadoactividad')
router.register(r'tipos-indicador', TipoIndicadorViewSet, basename='tipoindicador')
router.register(r'partidas-presupuestarias', PartidasPresupuestariasViewSet, basename='partidapresupuestaria')
router.register(r'departamentos', DepartamentosViewSet, basename='departamento')

urlpatterns = [
    path('', include(router.urls)),
]
