from django.urls import path
from . import views

urlpatterns = [
    # Vistas de especialidades

    path('listar_especialidades/', views.tabla_especialidades, name='tabla_especialidades'),
    path('especialidades/registrar/', views.registrar_especialidad, name='registrar_especialidad'),
    path('especialidades/editar/<int:especialidad_id>/', views.editar_especialidad, name='editar_especialidad'),
    path('especialidades/eliminar/<int:especialidad_id>/', views.eliminar_especialidad, name='eliminar_especialidad'),
]
