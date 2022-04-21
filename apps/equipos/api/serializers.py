"DRF Imports"
from rest_framework import serializers
"Local Imports"
from apps.equipos.models import Equipo

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'