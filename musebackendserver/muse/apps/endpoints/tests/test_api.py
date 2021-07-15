from rest_framework.exceptions import APIException
from apps.endpoints.models import Recommendation, Song
from unittest import mock

from django.test import TestCase
from rest_framework.test import APIClient

from .test_utils import populate_full_db, getSingleSpotifyTrackJSON, getTestSpotifyRecommendationJSON, getTestRecommendationSeedsJSON


def get_user_request_without_seeds():
    return {
        'spotifyObj': getSingleSpotifyTrackJSON()
    }

def get_user_request_with_seeds():
    return {
        'spotifyObj': getSingleSpotifyTrackJSON(),
        'seeds': getTestRecommendationSeedsJSON()
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

    def test_recommendations_without_seeds(self, get_song_recommendations):
        client = APIClient()
        payload = get_user_request_without_seeds()
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

    def test_recommendations_with_seeds(self, get_song_recommendations):
        client = APIClient()
        payload = get_user_request_with_seeds()
        response = client.post(self.url, payload, format='json')

        duplicates = 2
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data['recommendation_id'], str)
        self.assertEqual(len(response.data['recommended_track_ids']), 38)
        self.assertEqual(len(response.data['recommended_tracks']), 36)
        self.assertEqual(
            len(response.data['recommended_track_ids']) - duplicates, 
            len(response.data['recommended_tracks'])
        )


class TestSpiders(TestCase):

    @classmethod
    def setUpTestData(cls):
        '''
        Setup models for all tests in the class
        '''
        cls.recommendation_id = populate_full_db()
    
    def test_models_created_correctly(self):
        '''
        Check the data models are populated and linked together correctly
        '''
        songs = Song.objects.all()
        recommendations = Recommendation.objects.get(pk=self.recommendation_id)
        requested_song_ids = recommendations.userRequest.selectedTracks.all().values_list('track', flat=True)
        recommended_song_ids = recommendations.selectedTracks.all().values_list('track', flat=True)

        self.assertEqual(len(songs), 3)
        self.assertEqual(songs[0].id, requested_song_ids[0])
        self.assertEqual(songs[1].id, recommended_song_ids[0])
        self.assertEqual(songs[2].id, recommended_song_ids[1])

    @mock.patch('spiders.lyricraper.initiator.crawl', return_value='test_spider_job_id1234')
    def test_spider_start(self, crawl):
        '''
        Test spider job is started successfully for the given recommendation object ID
        '''
        client = APIClient()
        payload = {
            'recommendation_id': self.recommendation_id
        }
        url = '/api/spiders/start'
        response = client.post(url, payload, format='json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'spider_running')
        self.assertEqual(response.data['job_id'], 'test_spider_job_id1234')

    def test_lyrics_fetch(self):
        '''
        Test lyrics response is fetched correctly for the given recommendation object ID
        '''
        client = APIClient()
        payload = {
            'recommendation_id': self.recommendation_id
        }
        url = '/api/show_lyrics'
        response = client.post(url, payload, format='json')
        
        duplicates = 0
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data['recommendation_id'], str)
        self.assertEqual(len(response.data['recommended_track_ids']), 2)
        self.assertEqual(len(response.data['recommended_tracks']), 2)
        self.assertEqual(
            len(response.data['recommended_track_ids']) - duplicates, 
            len(response.data['recommended_tracks'])
        )

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
