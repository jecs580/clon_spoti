"""Serializador de Albums."""

# Django REST Framework
from rest_framework import serializers

# Models
from albums.models import Album


class AlbumModelSerializer(serializers.ModelSerializer):
    """Serializador de Albums."""

    class Meta:
        """Clase meta."""

        model = Album
        fields = '__all__'
