import json

from ..models import Song

from .constants import SPOTIFY_RECOMMENDATION_JSON, SPOTIFY_SONG_JSON, MODEL_SONGS_LIST


def populate_test_db():
    populate_with_queries()
    populate_with_songs()

def populate_with_queries():
    recommedation_list = ['nursery - bbno$', 'Reborn - KIDS SEE GHOSTS', 'SLOW DANCING IN THE DARK - Joji']
    recommendation_ids = [1, 2, 3]
    song_query_object = SongQueryObject(
        song_name = "cheapskate",
        artist_name = "oliver tree",
        recommendations = recommedation_list,
        recommendation_ids = str(recommendation_ids)[1:-1]
    )
    song_query_object.save()

def populate_with_songs():
    data = MODEL_SONGS_LIST

    for song in data:
        songToSave = Song(
            title=song['title'],
            main_artist=song['main_artist'],
            artist_info=song['artist_info'],
            all_artists=song['all_artists'],
            album=song['album_name'],
            spotify_id=song['spotify_id'],
            album_art_lg=song['album_art_lg'],
            album_art_md=song['album_art_md'],
            track_url=song['track_url'],
            preview_url=song['preview_url'],
            lyrics=song['lyrics']
        )
        songToSave.save()


def getSingleSpotifyTrackJSON():
    return SPOTIFY_SONG_JSON

def getTestSpotifyRecommendationJSON():
    recommendation_json = SPOTIFY_RECOMMENDATION_JSON
    return json.loads(recommendation_json)