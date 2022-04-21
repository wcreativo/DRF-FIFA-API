"Django Imports"
from django.db import models
"Third Party Imports"
from simple_history.models import HistoricalRecords
"Local Imports"
from apps.equipos.models import Equipo
from .managers import JugadorManager


class Jugador(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre del jugador')
    apellidos = models.CharField(max_length=255, verbose_name='Apellidos del jugador')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    posicion = models.CharField(max_length=255, verbose_name='Posición del jugador')
    numero_camiseta = models.IntegerField(verbose_name='Numero de camiseta')
    titular = models.BooleanField(default=True)
    foto = models.ImageField(verbose_name='Foto del jugador', blank=True, null=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    historical = HistoricalRecords()

    objects = JugadorManager()


    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"

    def __str__(self) -> str:
        return self.nombre
