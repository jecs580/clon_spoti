"""Admin de Album."""

# Django
from django.contrib import admin

# Model
from albums.models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """Admin de Album."""
    list_display = ('id', 'title', 'artist', 'year', 'description', 'portada')
    list_display_links = ('id', 'title')
    list_filter = ('created', 'modified', 'year')
    search_fields = ('title', 'year', 'artist__name')
    list_editable = ('portada', )
