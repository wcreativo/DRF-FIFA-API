"DRF Imports"
from lib2to3.refactor import RefactoringTool
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

"Python Imports"
import json

"Local Imports"
from .serializers import EquipoSerializer
from apps.equipos.models import Equipo

@api_view(['GET', 'POST'])
def equipo_api_view(request):

    if request.method == 'GET':
        equipos = Equipo.objects.all()
        equipos_serializer = EquipoSerializer(equipos, many=True)
        return Response(equipos_serializer.data, status.HTTP_200_OK)

    elif request.method == 'POST':
        equipos_serializer = EquipoSerializer(data = request.data)
        if equipos_serializer.is_valid():
            equipos_serializer.save()
            return Response(equipos_serializer.data, status.HTTP_201_CREATED)
        return Response(equipos_serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def equipo_detail_api_view(request, pk):

    if request.method == 'GET':
        equipo = Equipo.objects.filter(id=pk).first()
        equipo_serializer = EquipoSerializer(equipo)
        return Response(equipo_serializer.data, status.HTTP_200_OK)

    elif request.method == 'PUT':
        equipo = Equipo.objects.filter(id=pk).first()
        equipo_serializer = EquipoSerializer(equipo, data = request.data)
        if equipo_serializer.is_valid():
            equipo_serializer.save()
            return Response(equipo_serializer.data, status.HTTP_200_OK)
        return Response(equipo_serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        equipo = Equipo.objects.filter(id=pk).first()
        equipo.delete()
        return Response({'message': 'Equipo eliminado'}, status.HTTP_200_OK)


@api_view(['GET'])
def promedio_suplentes_api_view(request):
    promedio = Equipo.objects.promedio_suplentes_por_equipo()
    return Response({'Promedio_de_suplentes_por_equipo': promedio}, status.HTTP_200_OK)


@api_view(['GET'])
def total_equipos_registrados_api_view(request):
    total_equipos_registrados = Equipo.objects.total_equipos_registrados()
    return Response({'Total_equipos_registrados': total_equipos_registrados}, status.HTTP_200_OK)


@api_view(['GET'])
def equipo_mayor_numero_jugadores_api_view(request):
    equipo_mayor_numero_jugadores = Equipo.objects.equipo_mayor_numero_jugadores()
    return Response({'Equipo_mayor_numero_jugadores': equipo_mayor_numero_jugadores.nombre}, status.HTTP_200_OK)


@api_view(['GET'])
def promedio_jugadores_equipo_api_view(request):
    promedio_jugadores_por_equipo = Equipo.objects.promedio_jugadores_por_equipo()
    return Response({'Promedio_jugadores_por_equipo': promedio_jugadores_por_equipo}, status.HTTP_200_OK)

