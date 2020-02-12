"""URLs de Tracs."""

# Django
from django.urls import path, include

# Views
from .views import tracks as track_views

# Django REST Framework
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    r'tracks',
    track_views.TrackViewSet,
    basename='tracks'
)

urlpatterns = [
    path('', include(router.urls))
]