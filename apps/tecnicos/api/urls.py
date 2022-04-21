"Django Imports"
from django.urls import path
"Local Imports"
from apps.tecnicos.api.api import *

urlpatterns = [
    path('', tecnico_api_view, name='tecnicos_api'),
    path('detalle/<int:pk>/', tecnico_detail_api_view, name='tecnico_detail_api_view'),
    path('mas_viejo/', tecnico_mas_viejo_api_view, name='tecnico_mas_viejo_api_view'),
]