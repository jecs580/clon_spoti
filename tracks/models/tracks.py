""" Modelo de Pistas. """

# Django
from django.db import models

# Utilities
from utils.models import SpotiModel


class Track(SpotiModel):
    """Modelo de Pistas"""
    number_track = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)
    duration = models.PositiveSmallIntegerField()
    file = models.FileField(
        'Archivo de sonido',
        upload_to='uploads/tracks/',
        blank=True, null=True
    )
    album = models.ForeignKey('albums.Album', on_delete=models.CASCADE)

    def __str__(self):
        return 'cancion {} del album {}'.format(
            self.name,
            self.album.title
        )
