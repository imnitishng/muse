from django.test import TestCase
from rest_framework.test import APIClient

class EndpointTests(TestCase):

    def test_recommendations_view(self):
        client = APIClient()
        input_data = {
            "song": "Hurt",
            "artist": "Oliver Tree"
        }
        recommendations_url = "/api/v1/sp_recommedations"
        response = client.post(recommendations_url, input_data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], "OK")
        self.assertTrue("recommendations" in response.data)