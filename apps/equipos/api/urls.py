"Django Imports"
from django.urls import path
"Local Imports"
from apps.equipos.api.api import EquipoAPIView

urlpatterns = [
    path('', EquipoAPIView.as_view(), name='equipos_api'),
]