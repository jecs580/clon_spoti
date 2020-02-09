"""Admin Tracks."""

# Django
from django.contrib import admin

# Models
from tracks.models import Track


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    """Admin de Tracks."""
    list_display = ('id', 'number_track', 'name', 'album', 'duration', 'file')
    list_display_links = ('number_track', 'name')
    list_editable = ('file', )
    search_fields = ('number_track', 'name', 'album__title')
    list_filter = ('created', 'modified')
