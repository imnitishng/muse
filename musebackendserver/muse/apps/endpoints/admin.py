from django.contrib import admin

from .models import SongQueryObject, Songs, QueryStatus


class SongsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'all_artists', 'spotify_id', 'short_lyrics')

    def short_lyrics(self, obj):
        if obj.lyrics:
            shorts = obj.lyrics[:30]
        else:
            shorts =  ''
        return shorts

class SongsQueryAdmin(admin.ModelAdmin):
    list_display = ('id', 'song_name', 'artist_name', 'recommendations_count')

    def recommendations_count(self, obj):
        if obj.recommendation_ids:            
            return len(obj.recommendation_ids.split(','))
        else:
            return 0

# Register your models here.
admin.site.register(SongQueryObject, SongsQueryAdmin)
admin.site.register(Songs, SongsAdmin)
admin.site.register(QueryStatus)
