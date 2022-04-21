"Django Imports"
from django.db import models
from django.utils import timezone
from django.db.models.functions import ExtractYear
from django.db.models import Avg


class JugadorManager(models.Manager):

    def total_jugadores(self):
        return super().get_queryset().all().count()

    def jugador_mas_joven(self):
        return super().get_queryset().all().order_by('fecha_nacimiento').last()

    def jugador_mas_viejo(self):
        return super().get_queryset().all().order_by('fecha_nacimiento').first()

    def jugadores_suplentes(self):
        return super().get_queryset().filter(titular=False).count()

    def promedio_edad_jugadores(self):
        anio_actual = timezone.now().year
        return super().get_queryset().all().aggregate(promedio_edad = Avg(anio_actual - ExtractYear('fecha_nacimiento')))
