"Django Imports"
from django.db import models
"Third Party Imports"
from simple_history.models import HistoricalRecords
"Local Imports"
from apps.equipos.models import Equipo


class Rol(models.Model):
    rol = models.CharField(max_length=255, verbose_name='Rol')

    def __str__(self) -> str:
        return self.rol

class Cuerpo_Tecnico(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    apellidos = models.CharField(max_length=255, verbose_name='Apellidos')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    nacionalidad = models.CharField(max_length=255, verbose_name='Nacionalidad')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Cuerpo Técnico'
        verbose_name_plural = 'Cuerpo Técnico'

    def __str__(self) -> str:
        return self.nombre
