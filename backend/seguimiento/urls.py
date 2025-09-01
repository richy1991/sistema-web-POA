from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SeguimientoViewSet, BitacoraViewSet, BitacoraCambiosViewSet

router = DefaultRouter()
router.register(r'seguimientos', SeguimientoViewSet, basename='seguimiento')
router.register(r'bitacoras', BitacoraViewSet, basename='bitacora')
router.register(r'bitacoras-cambios', BitacoraCambiosViewSet, basename='bitacoracambios')

urlpatterns = [
    path('', include(router.urls)),
]
