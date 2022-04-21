"DRF Imports"
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

"Local Imports"
from .serializers import CuerpoTecnicoSerializer
from apps.tecnicos.models import Cuerpo_Tecnico

class TecnicosAPIView(APIView):

    def get(self, request):
        tecnicos = Cuerpo_Tecnico.objects.all()
        tecnicos_serializer = CuerpoTecnicoSerializer(tecnicos, many=True)
        return Response(tecnicos_serializer.data, status.HTTP_200_OK)