"DRF Imports"
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

"Local Imports"
from .serializers import CuerpoTecnicoSerializer
from apps.tecnicos.models import Cuerpo_Tecnico

@api_view(['GET', 'POST'])
def tecnico_api_view(request):

    if request.method == 'GET':
        tecnicos = Cuerpo_Tecnico.objects.all()
        tecnicos_serializer = CuerpoTecnicoSerializer(tecnicos, many=True)
        return Response(tecnicos_serializer.data, status.HTTP_200_OK)

    elif request.method == 'POST':
        tecnico_serializer = CuerpoTecnicoSerializer(data = request.data)
        if tecnico_serializer.is_valid():
            tecnico_serializer.save()
            return Response(tecnico_serializer.data, status.HTTP_201_CREATED)
        return Response(tecnico_serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tecnico_detail_api_view(request, pk):

    if request.method == 'GET':
        tecnico = Cuerpo_Tecnico.objects.filter(id=pk).first()
        tecnico_serializer = CuerpoTecnicoSerializer(tecnico)
        return Response(tecnico_serializer.data, status.HTTP_200_OK)

    elif request.method == 'PUT':
        tecnico = Cuerpo_Tecnico.objects.filter(id=pk).first()
        tecnico_serializer = CuerpoTecnicoSerializer(tecnico, data = request.data)
        if tecnico_serializer.is_valid():
            tecnico_serializer.save()
            return Response(tecnico_serializer.data, status.HTTP_200_OK)
        return Response(tecnico_serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        tecnico = Cuerpo_Tecnico.objects.filter(id=pk).first()
        tecnico.delete()
        return Response({'message': 'Técnico eliminado'}, status.HTTP_200_OK)