"Django Imports"
from django.urls import path
"Local Imports"
from apps.jugadores.api.api import JugadoresAPIView

urlpatterns = [
    path('', JugadoresAPIView.as_view(), name='jugadores_api'),
]