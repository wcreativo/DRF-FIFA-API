"DRF Imports"
from rest_framework import serializers
"Local Imports"
from apps.tecnicos.models import Cuerpo_Tecnico

class CuerpoTecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuerpo_Tecnico
        fields = '__all__'