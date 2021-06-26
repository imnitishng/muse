from django.contrib import admin

from .models import Song, UserRequest, Recommendation, SpotifyTrackSelection, UserTrackSelection


class SongsAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'title', 'all_artists', 'short_lyrics', 'created_at')

    def short_id(self, obj):
        return obj.id.hex[:8]
    
    def short_lyrics(self, obj):
        if obj.lyrics:
            shorts = obj.lyrics[:30]
        else:
            shorts =  ''
        return shorts


class UserRequestAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'linked_songs', 'spotifySeeds', 'created_at')

    def linked_songs(self, obj):
        return obj

    def short_id(self, obj):
        return obj.id.hex[:8]


class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'linked_songs', 'user_request_info', 'created_at')

    def user_request_info(self, obj):
        return f'{obj} | ID: {obj.userRequest.id}'

    def linked_songs(self, obj):
        return obj

    def short_id(self, obj):
        return obj.id.hex[:8]

class TracksToIDAdmin(admin.ModelAdmin):
    list_display = ('track', 'linked_object_ID')

    def linked_object_ID(self, obj):
        return obj.requestObject.id


# Register your models here.
admin.site.register(Song, SongsAdmin)
admin.site.register(UserRequest, UserRequestAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(SpotifyTrackSelection, TracksToIDAdmin)
admin.site.register(UserTrackSelection, TracksToIDAdmin)