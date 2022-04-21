"Django Imports"
from django.urls import path
"Local Imports"
from apps.equipos.api.api import *

urlpatterns = [
    path('', equipo_api_view, name='equipos_api'),
    path('detalle/<int:pk>/', equipo_detail_api_view, name='equipo_detail_api_view'),
    path('total_equipos_registrados/', total_equipos_registrados_api_view, name='total_equipos_registrados_api_view'),
    path('promedio_suplentes/', promedio_suplentes_api_view, name='promedio_suplentes_api_view'),
    path('equipo_mayor_numero_jugadores/', equipo_mayor_numero_jugadores_api_view, name='equipo_mayor_numero_jugadores_api_view'),
    path('promedio_jugadores_equipo/', promedio_jugadores_equipo_api_view, name='promedio_jugadores_equipo_api_view'),
]