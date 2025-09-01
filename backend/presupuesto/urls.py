from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemsPoaViewSet, EjecucionPresupuestariaViewSet

router = DefaultRouter()
router.register(r'items-poa', ItemsPoaViewSet, basename='itemspoa')
router.register(r'ejecucion-presupuestaria', EjecucionPresupuestariaViewSet, basename='ejecucionpresupuestaria')

urlpatterns = [
    path('', include(router.urls)),
]
