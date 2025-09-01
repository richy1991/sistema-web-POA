from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IndicadoresViewSet

router = DefaultRouter()
router.register(r'indicadores', IndicadoresViewSet, basename='indicador')

urlpatterns = [
    path('', include(router.urls)),
]
