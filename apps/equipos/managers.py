"Django Imports"
from django.db import models


class EquipoManager(models.Manager):
    def total_equipos_registrados(self):
        return super().get_queryset().all().count()

    def promedio_suplentes_por_equipo(self):
        equipos = super().get_queryset().all()
        suplentes = []
        for equipo in equipos:
            suplentes.append(equipo.jugador_set.filter(titular=False).count())
        return sum(suplentes) / len(suplentes)

    def equipo_mayor_numero_jugadores(self):
        return super().get_queryset().annotate(models.Count('jugador')).order_by('jugador__count').first()

    def promedio_jugadores_por_equipo(self):
        equipos = super().get_queryset().all()
        jugadores_por_equipo = []
        for equipo in equipos:
            jugadores_por_equipo.append(equipo.jugador_set.all().count())
        return sum(jugadores_por_equipo) / len(jugadores_por_equipo)
