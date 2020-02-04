""" Model general """

# Django
from django.db import models


class SpotiModel(models.Model):
    """Modelo base que heredaran las aplicaciones

    Este Modelos contendra campos para el fecha de creacion y modificacion
    """
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Fecha y hora en la cual se modifico el objeto'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Fecha y hora en la cual se modifico el objeto'
    )

    class Meta:
        """Clase Meta."""
        abstract = True
        # Especificamos que el ultimo en traer de los querys sera el ultimo creado
        get_latest_by = 'created'
        ordering = ['-created', '-modified']  # Colocamos que los objetos del modelo seran devueltos
        # ordenas en forma descendente por creacion, en le caso que haya coincidencia usara el de la modificacion
