"""Serializador de Tracks."""

# Django REST Framework
from rest_framework import serializers

# Models
from tracks.models import Track


class TrackModelSerializer(serializers.ModelSerializer):
    """Serializador de Tracks."""

    class Meta:
        """Clase Meta."""

        model = Track
        fields = '__all__'
