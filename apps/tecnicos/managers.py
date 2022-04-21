"Django Imports"
from django.db import models

class CuerpoTecnicoManager(models.Manager):

    def tecnico_mas_viejo(self):
        return super().get_queryset().all().order_by('fecha_nacimiento').first()