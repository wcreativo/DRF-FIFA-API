"DRF Imports"
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

"Local Imports"
from .serializers import JugadorSerializer
from apps.jugadores.models import Jugador


@api_view(['GET', 'POST'])
def jugador_api_view(request):

    if request.method == 'GET':
        jugadores = Jugador.objects.all()
        jugadores_serializer = JugadorSerializer(jugadores, many=True)
        return Response(jugadores_serializer.data, status.HTTP_200_OK)

    elif request.method == 'POST':
        jugador_serializer = JugadorSerializer(data = request.data)
        if jugador_serializer.is_valid():
            jugador_serializer.save()
            return Response(jugador_serializer.data, status.HTTP_201_CREATED)
        return Response(jugador_serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def jugador_detail_api_view(request, pk):

    if request.method == 'GET':
        jugador = Jugador.objects.filter(id=pk).first()
        jugador_serializer = JugadorSerializer(jugador)
        return Response(jugador_serializer.data, status.HTTP_200_OK)

    elif request.method == 'PUT':
        jugador = Jugador.objects.filter(id=pk).first()
        jugador_serializer = JugadorSerializer(jugador, data = request.data)
        if jugador_serializer.is_valid():
            jugador_serializer.save()
            return Response(jugador_serializer.data, status.HTTP_200_OK)
        return Response(jugador_serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        jugador = Jugador.objects.filter(id=pk).first()
        jugador.delete()
        return Response({'message': 'Jugador eliminado'}, status.HTTP_200_OK)


@api_view(['GET'])
def total_jugadores_api_view(request):
    total_jugadores = Jugador.objects.total_jugadores()
    return Response({'Total_jugadores': total_jugadores}, status.HTTP_200_OK)


@api_view(['GET'])
def jugador_mas_joven_api_view(request):
    jugador_mas_joven = Jugador.objects.jugador_mas_joven()
    return Response({'Jugador_mas_joven': jugador_mas_joven.nombre}, status.HTTP_200_OK)

@api_view(['GET'])
def jugador_mas_viejo_api_view(request):
    jugador_mas_viejo = Jugador.objects.jugador_mas_viejo()
    return Response({'Jugador_mas_viejo': jugador_mas_viejo.nombre}, status.HTTP_200_OK)

@api_view(['GET'])
def suplentes_api_view(request):
    suplentes = Jugador.objects.jugadores_suplentes()
    return Response({'Jugadores_suplentes': suplentes}, status.HTTP_200_OK)

@api_view(['GET'])
def promedio_edad_jugadores_api_view(request):
    promedio_edad = Jugador.objects.promedio_edad_jugadores()
    return Response({'Promedio_edad_jugadores': promedio_edad}, status.HTTP_200_OK)


