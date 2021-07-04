from unittest import mock

from django.test import TestCase
from rest_framework.test import APIClient

from .usencoder.model import UniversalSentenceEncoder
from apps.endpoints.tests.test_utils import populate_full_db, getTestRanks, getModelRanksResponse


@mock.patch('apps.nlp.usencoder.model.UniversalSentenceEncoder.get_model_results', return_value=getTestRanks())
@mock.patch('apps.nlp.views.ModelView.buildresponse', return_value=getModelRanksResponse())
class NLPTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        '''
        Setup models for all tests in the class
        '''
        cls.recommendation_id = populate_full_db()

    def test_getting_ranks_full(self, get_model_results, buildresponse):
        """
        Test the of the model to get embeddings and ranks of 
        the lyrics using the model and recommendations ID specified.
        """
        client = APIClient()

        input_data = {
            'recommendation_id': self.recommendation_id,
            'model_code': 'use'
        }
        url = '/api/get_embeddings'
        response = client.post(url, input_data, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'success')
        self.assertIn('ranks', response.data)
