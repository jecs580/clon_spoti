""""Album app."""
# Este archivo sirve para declarar a django nuestras aplicaciones, las variables que deben estar si o si son: "name" y "verbose name" pero tu le puedes agregar mas cosas si quieres.

# Django
from django.apps import AppConfig

# El nombre de la clase sirve para instalarlo en INSTALLED_APPS en los settings
class AlbumsAppConfig(AppConfig):
    """"Configuracion de la app de Albums."""
    name= 'albums'
    verbose_name='Albums' # El nombre "bonito" :V

