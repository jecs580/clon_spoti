"""Vistas de Tracks."""

# Django REST Framework
from rest_framework.viewsets import ModelViewSet

# Model
from tracks.models import Track

# Serializers
from tracks.serializers import TrackModelSerializer


class TrackViewSet(ModelViewSet):
    """Vista de Tracks."""

    queryset = Track.objects.all()
    serializer_class = TrackModelSerializer
