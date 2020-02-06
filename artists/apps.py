""""Artist app."""
# Este archivo sirve para declarar a django nuestras aplicaciones, las variables que deben estar si o si son: "name" y "verbose name" pero tu le puedes agregar mas cosas si quieres.

# Django
from django.apps import AppConfig

# El nombre de la clase sirve para instalarlo en INSTALLED_APPS en los settings
class ArtistsAppConfig(AppConfig):
    """"Configuracion de la app de Artistas."""
    name= 'artists'
    verbose_name='Artists' # El nombre "bonito" :V

