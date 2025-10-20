from django.urls import path
from . import views

urlpatterns = [
    # Vistas de servicios
    path('listar_servicio/', views.tabla_servicios, name='tabla_servicios'),
    path('servicios/registrar/', views.registrar_servicio, name='registrar_servicio'),
    path('servicios/editar/<int:servicio_id>/', views.editar_servicio, name='editar_servicio'),
    path('servicios/eliminar/<int:servicio_id>/', views.eliminar_servicio, name='eliminar_servicio'),
]
