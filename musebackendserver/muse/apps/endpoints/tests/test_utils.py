import json, requests

from ..services.spotify import SpotifyService
from ..serializers import SongSerializer

from .constants import SPOTIFY_RECOMMENDATION_JSON, SPOTIFY_SONG_JSON, MODEL_SONGS_LIST


def getTestRanks():
    res = requests.Response()
    res.status_code = 200
    res._content = b'{"status": "success", "ranks": "testranks"}'
    return res

def getModelRanksResponse():
    return {
        'asdasd': 0.32,
        'qweadf': 0.69,
        'fghfgb': 0.52
    }

def populate_full_db():
    saved_songs = populate_songs()
    recommendations_obj = populate_parent_models(saved_songs)
    return recommendations_obj.id.hex

def populate_parent_models(saved_songs):
    spotify_service = SpotifyService()
    user_request_songs = [saved_songs[0]]
    spotify_recommended_songs = list(saved_songs[1:])

    # Create and link parent objects
    user_request_object = spotify_service.save_user_query_to_model()
    spotify_service.link_songs_to_parent_objects(user_request_songs, user_request_object)
    recommendations = spotify_service.save_recommendation_object_to_model(user_request_object)
    spotify_service.link_songs_to_parent_objects(spotify_recommended_songs, recommendations)

    return recommendations

def populate_songs():
    songs_list = MODEL_SONGS_LIST
    serialized_data = SongSerializer(data=songs_list, many=True)
    if serialized_data.is_valid():
        saved_data = serialized_data.save()
        return saved_data

def getSingleSpotifyTrackJSON():
    return SPOTIFY_SONG_JSON

def getTestSpotifyRecommendationJSON():
    recommendation_json = SPOTIFY_RECOMMENDATION_JSON
    return json.loads(recommendation_json)