"DRF Imports"
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

"Local Imports"
from .serializers import EquipoSerializer
from apps.equipos.models import Equipo

class EquipoAPIView(APIView):

    def get(self, request):
        equipos = Equipo.objects.all()
        equipos_serializer = EquipoSerializer(equipos, many=True)
        return Response(equipos_serializer.data, status.HTTP_200_OK)



