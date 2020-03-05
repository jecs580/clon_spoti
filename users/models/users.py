"""Modelo de Usuarios Personalizado"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from utils.models import SpotiModel


class User(SpotiModel, AbstractUser):
    """Modelo de Usuarios."""
    email = models.EmailField(
        'correo electrico',
        unique=True,  # Estableceremos como identificador el correo,
        # no puede haber correos repetidos
        # Mensaje de error al momento de repetir correo
        error_messages={'unique': 'Correo electronico ya existente'}
    )
    picture = models.ImageField(
        'foto de perfil del usuario',
        upload_to='users/pictures/',
        blank=True, null=True
    )
    is_verified = models.BooleanField(
        'verificado',
        default=False,
        help_text=(
            'Establece verdadero cuando el usuario haya verificado su email')
    )

    USERNAME_FIELD = 'email'  # Establecemos el email como nuevo identificador.
    # Campos que seran requeridos al
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    # momento de crear objetos de tipo User.
    is_client = models.BooleanField(
        'cliente',
        default=True,
        help_text=(
            'Variable booleana que sirve para distinguir los clients que escuchan la musica de los que suben')
    )

    def __str__(self):
        """Regresamos el username

        Esto es posible por que usamos el modelo abstractUser que por
        defecto ya trae el username
        """
        return self.username

    def get_short_name(self):
        """Regresamos el username.

        Sobre escribiendo el metedo para que tambien nos devuelva el username.
        """
        return self.username
