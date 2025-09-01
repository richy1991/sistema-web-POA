from django.urls import path
from .views import PoaExcelReportView, PoaPdfReportView

urlpatterns = [
    path('poa-excel/', PoaExcelReportView.as_view(), name='reporte-poa-excel'),
    path('poa-pdf/<int:poa_id>/', PoaPdfReportView.as_view(), name='reporte-poa-pdf'),
]
