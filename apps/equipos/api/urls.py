"Django Imports"
from django.urls import path
"Local Imports"
from apps.equipos.api.api import equipo_api_view, equipo_detail_api_view

urlpatterns = [
    path('', equipo_api_view, name='equipos_api'),
    path('detalle/<int:pk>/', equipo_detail_api_view, name='equipo_detail_api_view'),
]