"""Modulo principal de URLs."""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('artists.urls', 'artists'), namespace='artists')),
    path('', include(('albums.urls', 'albums'), namespace='albums')),
    path('', include(('tracks.urls', 'tracks'), namespace='tracks')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
