"Django Imports"
from django.urls import path
"Local Imports"
from apps.tecnicos.api.api import tecnico_api_view, tecnico_detail_api_view

urlpatterns = [
    path('', tecnico_api_view, name='tecnicos_api'),
    path('detalle/<int:pk>/', tecnico_detail_api_view, name='tecnico_detail_api_view'),
]