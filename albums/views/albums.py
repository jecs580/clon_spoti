"""Vistas de Albums."""

# Django REST Framework
from rest_framework.viewsets import ModelViewSet

#Models
from albums.models import Album

# Serializers
from albums.serializers import AlbumModelSerializer


class AlbumViewSet(ModelViewSet):
    """Vistas del Album"""

    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer
