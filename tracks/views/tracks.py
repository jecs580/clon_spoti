"""Vistas de Tracks."""

# Django REST Framework
from rest_framework.viewsets import ModelViewSet

# Model
from tracks.models import Track

# Serializers
from tracks.serializers import TrackModelSerializer

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

class TrackViewSet(ModelViewSet):
    """Vista de Tracks."""
    permission_classes=[IsAuthenticated]
    queryset = Track.objects.all()
    serializer_class = TrackModelSerializer
