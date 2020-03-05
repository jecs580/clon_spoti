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
        # Especificamos que el ultimo objeto en traer de los querys
        # sera el ultimo creado
        get_latest_by = 'created'
        ordering = ['-created', '-modified']  # Colocamos que los
        # objetos del modelo seran devueltos
        # ordena en forma descendente por creacion,en caso que haya
        # coincidencia usara el campo de modificacion
