"""Urls de Artists."""

# Django
from django.urls import path, include

# Views
from .views import artists as artist_views

# Django REST Framework
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    r'artists',  # Ruta raiz que buscara
    artist_views.ArtistViewSet,  # Vista relacioanada
    basename='artist'
    )

urlpatterns = [
    path('', include(router.urls))
]
