from django.urls import path
from . import views

urlpatterns = [
    # Vistas de reportes 
    path('editar_reporte/', views.editar_reporte, name='editar_reporte'),
    path('tabla_reportes/', views.tabla_reportes, name='tabla_reportes'),
]
