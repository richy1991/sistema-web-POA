from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PoaViewSet,
    ObjetivoEspecificoViewSet,
    ActividadPoaViewSet,
    ActividadPoaResponsablesViewSet,
    CronogramaPoaViewSet,
)

router = DefaultRouter()
router.register(r'poas', PoaViewSet, basename='poa')
router.register(r'objetivos-especificos', ObjetivoEspecificoViewSet, basename='objetivoespecifico')
router.register(r'actividades-poa', ActividadPoaViewSet, basename='actividadpoa')
router.register(r'actividades-responsables', ActividadPoaResponsablesViewSet, basename='actividadresponsable')
router.register(r'cronogramas-poa', CronogramaPoaViewSet, basename='cronogramapoa')

urlpatterns = [
    path('', include(router.urls)),
]
