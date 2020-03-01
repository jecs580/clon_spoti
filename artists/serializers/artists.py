"""Serializador de Artistas."""

# Django REST Framework
from rest_framework import serializers

# Models
from artists.models import Artist


class ArtistModelSerializer(serializers.ModelSerializer):
    """Serializador para el modelo de Artistas."""

    class Meta:
        """Clase Meta."""
        model = Artist
        fields = '__all__'
