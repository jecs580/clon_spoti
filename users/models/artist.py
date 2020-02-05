"""Modelo de Artistas."""

# Django
from django.db import models

# Utilities
from utils.models import SpotiModel


class Artist(SpotiModel):
    """Modelo de artista."""
    name=models.CharField(
        'Nombre Artistico',
        max_length=64,
        unique=True,
        error_messages={'unique': 'Nombre de artista ya existente'}
    )
    description = models.TextField(
        'description del artista',
        null=True, blank=True
    )
    image = models.ImageField(
        'foto del Artista',
        upload_to='artist/pictures/',
        blank=True, null=True
    )

    def __str__(self):
        """Retorna el nombre del Artista."""
        return self.name
