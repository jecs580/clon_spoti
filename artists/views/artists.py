"""Vista de Artistas."""

# Django REST Framework
from rest_framework.viewsets import ModelViewSet

# Models
from artists.models import Artist

# Serializers
from artists.serializers import ArtistModelSerializer

class ArtistViewSet(ModelViewSet):
    """Conjunto de vistas de Artistas."""

    queryset = Artist.objects.all()
    serializer_class = ArtistModelSerializer
