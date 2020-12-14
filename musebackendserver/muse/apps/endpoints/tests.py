from django.test import TestCase
from rest_framework.test import APIClient

from .models import SongQueryObject
from .test_utils import populate_test_db

class EndpointTests(TestCase):

    def test_recommendations_view(self):
        client = APIClient()
        input_data = {
            "song": "cheapskate",
            "artist": "oliver tree"
        }
        recommendations_url = "/api/v1/sp_recommedations"
        response = client.post(recommendations_url, input_data, format="json")
        
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], "OK")
        self.assertTrue("recommendations" in response.data)

    def test_lyrics_fetch(self):
        client = APIClient()
        populate_test_db()

        input_data = {
            "query_id": "1"
        }
        lyrics_url = "/api/v1/get_lyrics"
        response = client.post(lyrics_url, input_data, format="json")
        
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], "OK")