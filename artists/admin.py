"""Admin de Artista."""

# Django
from django.contrib import admin

# Model
from artists.models import Artist


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    """Admin de Artistas."""
    list_display = ('id', 'name', 'image', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_filter = ('created', 'modified')
    list_editable = ('image', )
