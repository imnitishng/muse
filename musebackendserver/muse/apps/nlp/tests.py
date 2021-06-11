import inspect
from django.test import TestCase
from rest_framework.test import APIClient

from .usencoder.model import UniversalSentenceEncoder
from .registry import MLRegistry
from apps.endpoints.test_utils import populate_test_db

class NLPTests(TestCase):

    def test_registry(self):
        """
        Test NLP model registry
        """
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "universal_sentence_encoder"
        algorithm_object = UniversalSentenceEncoder()
        algorithm_name = "Universal Sentence Encoder"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "Nitish"
        algorithm_description = "Create sentence embeddings"
        algorithm_code = inspect.getsource(UniversalSentenceEncoder)

        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        self.assertEqual(len(registry.endpoints), 1)

    def test_getting_ranks_full(self):
        """
        Test the final response of model to get the songs with 
        their respective ranks.

        [attrs]: 
        `type`: type of the request to be sent 
            full - song ID and lyrics; semi - only song ID
        `songs`: dump of song IDs and names in the case of `full` type, 
        only song IDs in `semi` type
        `model`: Name of the model to use
        Currently available models - 
            use - Universal Sentence Encoder
        """
        populate_test_db()
        client = APIClient()

        input_data = {
            'type': 'full',
            'songs': [
                {'1': 'ok man'},
                {'2': 'ok dud'}
            ],
            'model': 'use'
        }

        url = '/api/get_embeddings'
        response = client.post(url, input_data, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'OK')
        self.assertIn('ranks', response.data)

    def test_getting_ranks_semi(self):
        """
        Test the final response of model to get the songs with 
        their respective ranks.

        [attrs]: 
        `type`: type of the request to be sent 
            semi - only song ID
        `songs`: dump of song IDs and names in the case of `full` type, 
        only song IDs in `semi` type
        `model`: Name of the model to use
        Currently available models - 
            use - Universal Sentence Encoder
        """
        populate_test_db()
        client = APIClient()

        input_data = {
            'type': 'semi',
            'songs': [
                '1', '2', '3'
            ],
            'model': 'use'
        }

        url = '/api/get_embeddings'
        response = client.post(url, input_data, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'OK')
        self.assertIn('ranks', response.data)
