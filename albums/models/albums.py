"""Modelo Album. """

# Django
from django.db import models

# Utilities
from utils.models import SpotiModel


class Album(SpotiModel):
    """Modelo de Album"""

    title = models.CharField(
        'ttulo del album',
        unique=True,
        max_length=60
    )
    artist = models.ForeignKey(
        'artists.Artist',on_delete=models.CASCADE,
        help_text='Artista que pertenece el album',
    )
    description = models.TextField(
        help_text='Descripcion del Album',
        max_length=250,
        null=True, blank=True
    )
    year = models.PositiveSmallIntegerField(
        'year',
        default=0,
        help_text='Anio de publicacion de album'
    )
    portada = models.ImageField(
    'foto de portada',
    upload_to='albums/portadas/',
    blank=True, null=True
    )
    
    def __str__(self):
        """Retorna titulo del album mas su Artista."""
        return 'Album {} por {}'.format(
            self.title,
            self.artist.name
        )

