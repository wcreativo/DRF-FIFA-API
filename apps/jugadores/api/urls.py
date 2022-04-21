"Django Imports"
from django.urls import path
"Local Imports"
from apps.jugadores.api.api import *

urlpatterns = [
    path('', jugador_api_view, name='jugadores_api'),
    path('detalle/<int:pk>/', jugador_detail_api_view, name='jugador_detail_api_view'),
    path('total_jugadores/', total_jugadores_api_view, name='total_jugadores_api_view'),
    path('jugador_mas_joven/', jugador_mas_joven_api_view, name='jugador_mas_joven_api_view'),
    path('jugador_mas_viejo/', jugador_mas_viejo_api_view, name='jugador_mas_viejo_api_view'),
    path('suplentes/', suplentes_api_view, name='suplentes_api_view'),
    path('promedio_edad/', promedio_edad_jugadores_api_view, name='promedio_edad_api_view'),
]