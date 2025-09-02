from django.urls import path
from .views import (
    PersonaList, PersonaByDocumento, ActualizarPersona, CrearPersona, EliminarPersona,
    TareaList, CrearTarea, ActualizarTarea, EliminarTarea, TareaByFechaLimite
)

urlpatterns = [
    path('personas/', PersonaList.as_view(), name='persona-list'),
    path('personas/crear/', CrearPersona.as_view(), name='persona-crear'),
    path('personas/actualizar/<int:pk>/', ActualizarPersona.as_view(), name='persona-actualizar'),
    path('personas/documento/<str:documento>/', PersonaByDocumento.as_view(), name='persona-por-documento'),
    path('personas/eliminar/<int:pk>/', EliminarPersona.as_view(), name='persona-eliminar'),
    path('tareas/', TareaList.as_view(), name='tarea-list'),
    path('tareas/crear/', CrearTarea.as_view(), name='tarea-crear'),
    path('tareas/actualizar/<int:pk>/', ActualizarTarea.as_view(), name='tarea-actualizar'),
    path('tareas/eliminar/<int:pk>/', EliminarTarea.as_view(), name='tarea-eliminar'),
    path('tareas/fecha_limite/<str:fecha_limite>/', TareaByFechaLimite.as_view(), name='tarea-por-fecha-limite')
]