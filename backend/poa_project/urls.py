from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT Token Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API endpoints for modular apps (in Spanish)
    # The path is the URL, the include is the python module
    path('api/accounts/', include('cuentas.urls')),
    path('api/core/', include('nucleo.urls')),
    path('api/poa/', include('poa.urls')),
    path('api/indicators/', include('indicadores.urls')),
    path('api/budget/', include('presupuesto.urls')),
    path('api/tracking/', include('seguimiento.urls')),
    path('api/reports/', include('reportes.urls')),
    path('api/adminpanel/', include('panel_administracion.urls')),
]
