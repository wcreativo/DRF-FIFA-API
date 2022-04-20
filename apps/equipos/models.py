"Django Imports"
from django.db import models
"Third Party Imports"
from simple_history.models import HistoricalRecords


class Equipo(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre del Equipo')
    bandera = models.ImageField(verbose_name='Bandera del equipo')
    escudo = models.ImageField(verbose_name='Escudo del equipo')
    historical = HistoricalRecords()

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

    def __str__(self) -> str:
        return self.nombre
