"DRF Imports"
from rest_framework import serializers
"Local Imports"
from apps.jugadores.models import Jugador

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = '__all__'