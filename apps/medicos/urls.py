from django.urls import path
from . import views

urlpatterns = [
    # Vistas de medicos

    path('listar_medicos/', views.tabla_medicos, name='tabla_medicos'),
    path('medicos/registrar/', views.registrar_medico, name='registrar_medico'),
    path('medicos/editar/<int:medico_id>/', views.editar_medico, name='editar_medico'),
    path('medicos/eliminar/<int:medico_id>/', views.eliminar_medico, name='eliminar_medico'),
]
