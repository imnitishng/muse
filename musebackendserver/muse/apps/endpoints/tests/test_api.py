from unittest import mock

from django.test import TestCase
from rest_framework.test import APIClient

from .test_utils import populate_test_db, getSingleSpotifyTrackJSON, getTestSpotifyRecommendationJSON


def get_complete_user_request():
    return {
        'song': 'cheapskate',
        'artist': 'oliver tree',
        'spotifyObj': getSingleSpotifyTrackJSON()
    }

def get_incomplete_user_request():
    return {
        'song': 'cheapskate',
        'artist': 'oliver tree',
    }


@mock.patch('apps.endpoints.services.spotify.SpotifyService.get_song_recommendations', return_value=getTestSpotifyRecommendationJSON())
class TestSpotifyRecommendations(TestCase):
    '''
    Test API response for fetching Spotify Recommendations, only one copy of a track object
    is sent in the response in order to reduce data redundancy. Hence `recommended_track_ids`
    and `recommended_tracks` are unequal because of 2 same tracks in the recommendation response
    This will practically never happen in real case because Spotify isn't stupid to recommend you
    duplicate tracks in a single response.
    '''

    url = '/api/spotify/recommendations'

    def test_recommendations_complete_request(self, get_song_recommendations):
        client = APIClient()
        payload = get_complete_user_request()
        response = client.post(self.url, payload, format='json')

        # Explicitly defining duplicates for a rare test case
        duplicates = 2
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data['recommendation_id'], str)
        self.assertEqual(len(response.data['recommended_track_ids']), 38)
        self.assertEqual(len(response.data['recommended_tracks']), 36)
        self.assertEqual(
            len(response.data['recommended_track_ids']) - duplicates, 
            len(response.data['recommended_tracks'])
        )

    def test_recommendations_incomplete_request(self, get_song_recommendations):
        client = APIClient()
        payload = get_incomplete_user_request()
        response = client.post(self.url, payload, format='json')

        self.assertEqual(response.status_code, 400)


class TestSpiders(TestCase):
    pass
    
    # def test_lyrics_fetch(self):
    #     client = APIClient()
    #     populate_test_db()

    #     payload = {
    #         'query_id': '1'
    #     }
    #     url = '/api/show_lyrics'
    #     response = client.post(url, payload, format='json')
        
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data['status'], 'OK')

    # def test_fetch_accesstoken(self):
    #     client = APIClient()

    #     url = '/api/spotify/accesstoken'
    #     response = client.get(url)
        
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('access_token', response.data)

    # def test_spider_jobs_status(self):
    #     client = APIClient()

    #     url = '/api/spiders/status'
    #     response = client.get(url)
        
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('running', response.data)


class TestModels(TestCase):
    pass
