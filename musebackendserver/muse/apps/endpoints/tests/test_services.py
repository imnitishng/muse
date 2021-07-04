import json

from unittest import mock

from django.test import TestCase
from rest_framework.exceptions import APIException

from ..services.spotify import SpotifyService
from ..serializers import SongRequestSerializer
from .test_api import get_complete_user_request
from .test_utils import getTestSpotifyRecommendationJSON
from .constants import TWO_DUPLICATE_SPOTIFY_SONGS


def get_serialized_request_data():
    request = get_complete_user_request()
    request_serializer = SongRequestSerializer(data=request)
    if request_serializer.is_valid():
        return request_serializer.data
    return None

def getTwoDuplicateSongs():
    return json.loads(TWO_DUPLICATE_SPOTIFY_SONGS)


class TestSpotifyService(TestCase):

    @classmethod
    def setUpTestData(cls):
        '''
        Setup serialized data only once for all the tests in the class
        '''
        cls.safe_request_data = get_serialized_request_data()
        cls.spotify_service = SpotifyService()

    def test_serialized_data_initialzes_service(self):
        '''
        Test only serialized can initialized the tracks in Spotify service
        '''
        trackObj = self.safe_request_data.get("spotifyObj")
        self.spotify_service.initialize_track_from_request(trackObj)

        self.assertEqual(self.spotify_service.trackInFocusID, '11dFghVXANMlKmJXsNCbNl')
        self.assertEqual(self.spotify_service.trackArtistID, '6sFIWsNpZYqfjUpaCgueju')

    def test_unserialized_data_raises_exception(self):
        '''
        Test invalid or raw data raises exception when initializing service
        '''
        trackObj = {
            'tracks': 'broken track',
            'artists': 'broken artist',
            'id': '2343'
        }

        self.assertRaises(
            AttributeError, 
            lambda: self.spotify_service.initialize_track_from_request(trackObj)
        )

    def test_save_songs_from_query(self):
        '''
        Test single track from user request is saved in the database
        '''
        trackObj = self.safe_request_data.get("spotifyObj")
        _, __, saved_songs_list = self.spotify_service.save_songs_from_query(trackObj)
        saved_song = saved_songs_list[0]

        self.assertEqual(len(saved_songs_list), 1)
        self.assertEqual(saved_song.title, 'Cut To The Feeling')
        self.assertEqual(saved_song.spotify_id, '11dFghVXANMlKmJXsNCbNl')


    def test_get_song_recommendations_unintialized(self):
        '''
        Test spotify recommendations are not fetched when service is not initialized with 
        requested track from the user.
        '''
        self.assertRaises(APIException, lambda: self.spotify_service.get_song_recommendations(None))

    @mock.patch('apps.endpoints.services.spotify.SpotifyService.get_song_recommendations', return_value=getTestSpotifyRecommendationJSON())
    def test_get_song_recommendations_intialized(self, get_song_recommendations):
        '''
        Test fetching spotify recommendations with properly initialized service data, for default seeds
        '''
        seeds = None
        response = self.spotify_service.get_song_recommendations(seeds)

        self.assertEqual(len(response), 2)
        self.assertEqual(len(response['tracks']), 43)
        
    def test_parent_objects_creation(self):
        '''
        Test create `UserRequest`, `Recommendation`object is saved successfully for default seeds
        in sequence. Raises APIException with invalid arguments.
        '''
        seeds = None
        saved_user_request = self.spotify_service.save_user_query_to_model(seeds)
        saved_recommendation = self.spotify_service.save_recommendation_object_to_model(saved_user_request)
        
        self.assertEqual(saved_user_request.spotifySeeds, 'default')
        self.assertEqual(saved_recommendation.userRequest, saved_user_request)

        self.assertRaises(APIException, lambda: self.spotify_service.save_recommendation_object_to_model(None))

    @mock.patch('apps.endpoints.services.spotify.SpotifyService.get_song_recommendations', return_value=getTestSpotifyRecommendationJSON())
    def test_link_songs_to_parent_objects(self, get_song_recommendations):
        '''
        Test creation of foreign key mapping of tracks to respective user request and 
        recommendation objects
        '''
        trackObj = self.safe_request_data.get("spotifyObj")
        self.spotify_service.initialize_track_from_request(trackObj)
        _, __, saved_requested_songs = self.spotify_service.save_songs_from_query(trackObj)
        user_request = self.spotify_service.save_user_query_to_model(seeds=None)
        self.spotify_service.link_songs_to_parent_objects(saved_requested_songs, user_request)

        spotifyRecommendationsDict = self.spotify_service.get_song_recommendations(None)
        recommendations = self.spotify_service.save_recommendation_object_to_model(user_request)
        _, __, saved_recommended_songs = self.spotify_service.store_songs_to_model(spotifyRecommendationsDict.get('tracks'))
        saved_song_object_links = self.spotify_service.link_songs_to_parent_objects(saved_recommended_songs, recommendations)

        self.assertEqual(len(saved_song_object_links), len(saved_recommended_songs))

    def test_duplicate_songs_not_stored(self):
        '''
        Test duplicate songs are not stored as a new entry in the database
        '''
        tracks = getTwoDuplicateSongs()
        saved_songs, fetched_songs, all_recommended_songs = self.spotify_service.store_songs_to_model(tracks)

        self.assertEqual(len(tracks), 2)
        self.assertEqual(len(saved_songs), 1)
        self.assertEqual(len(fetched_songs), 1)
        self.assertEqual(len(all_recommended_songs), 2)