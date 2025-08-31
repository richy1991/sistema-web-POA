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

    # API endpoints for modular apps
    path('api/accounts/', include('accounts.urls')),
    path('api/core/', include('core.urls')),
    path('api/poa/', include('poa.urls')),
    path('api/indicators/', include('indicators.urls')),
    path('api/budget/', include('budget.urls')),
    path('api/tracking/', include('tracking.urls')),
    path('api/reports/', include('reports.urls')),
    path('api/adminpanel/', include('adminpanel.urls')),
]
