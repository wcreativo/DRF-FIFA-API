"Django Imports"
from django.urls import path
"Local Imports"
from apps.jugadores.api.api import jugador_api_view, jugador_detail_api_view

urlpatterns = [
    path('', jugador_api_view, name='jugadores_api'),
    path('detalle/<int:pk>/', jugador_detail_api_view, name='jugador_detail_api_view'),
]