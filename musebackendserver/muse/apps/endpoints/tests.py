from django.test import TestCase
from rest_framework.test import APIClient

from .models import SongQueryObject
from .test_utils import populate_test_db

class EndpointTests(TestCase):

    def test_recommendations_view(self):
        client = APIClient()
        
        payload = {
            "song": "cheapskate",
            "artist": "oliver tree"
        }
        url = "/api/v1/sp_recommedations"
        response = client.post(url, payload, format="json")
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["query_id"], 1)
        self.assertEqual(len(response.data["recommendations"]), 50)
        self.assertEqual(len(response.data["recommendation_ids"]), 50)

    def test_lyrics_fetch(self):
        client = APIClient()
        populate_test_db()

        payload = {
            "query_id": "1"
        }
        url = "/api/v1/show_lyrics"
        response = client.post(url, payload, format="json")
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], "OK")