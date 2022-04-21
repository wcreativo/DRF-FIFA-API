"DRF Imports"
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

"Local Imports"
from .serializers import JugadorSerializer
from apps.jugadores.models import Jugador

class JugadoresAPIView(APIView):

    def get(self, request):
        jugadores = Jugador.objects.all()
        jugadores_serializer = JugadorSerializer(jugadores, many=True)
        return Response(jugadores_serializer.data, status.HTTP_200_OK)