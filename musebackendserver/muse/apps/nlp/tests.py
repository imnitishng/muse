import inspect
from django.test import TestCase

from .usencoder.model import LyricsEncoderModel
from .registry import MLRegistry

class NLPTests(TestCase):

    def test_data_preprocessing(self):
        """
        Test the data preprocessing for model
        """
        input_data = {
            "song": ["Joy - Bastille"],
            "lyrics": ["""
            [Verse 1]
            Thought I'd never be waking on the kitchen floor
            But here I lie, not the first time
            Now my morning has broken, and it brings the fear
            My mind's falling, fall in

            [Pre-Chorus]
            Then I feel my pulse quickening
            But regrets can't change anything
            Yeah, I feel my pulse quickening
            When your name lights up the screen

            [Chorus]
            Oh joy, when you call me
            I was giving up, oh, I was giving in
            Joy, set my mind free
            I was giving up, oh, I was giving in

            [Post-Chorus]
            How d'you always know when I'm down?
            How d'you always know when I'm down?

            [Verse 2]
            Take a walk through the wreckage, clearing out my head
            I hear your eyes roll right down the phone
            I'm your walking disaster, keep on dragging me
            From self-pity, poor me

            [Pre-Chorus]
            Then I feel my pulse quickening
            But I wouldn't change a thing

            [Chorus]
            Oh joy, when you call me
            I was giving up, oh, I was giving in
            Joy, set my mind free
            I was giving up, oh, I was giving in

            [Post-Chorus]
            How d'you always know when I'm down?
            How d'you always know when I'm down?

            [Bridge]
            As the night dissolves into this final frame
            You're a sweet relief, you saved me from my brain
            From my brain, from my brain, from my brain
            Oh, oh, oh, oh

            [Chorus]
            Oh joy, when you call me
            I was giving up, oh, I was giving in
            Joy, set my mind free
            I was giving up, oh, I was giving in

            [Post-Chorus]
            How d'you always know when I'm down?
            How d'you always know when I'm down?

            [Outro]
            I feel joy when you call me
            I feel joy when you call me (I-I-I feel joy)
            I feel joy when you call me
            I feel joy when you call me
            How d'you always know when I'm down?
            How d'you always know when I'm down?
            """]
        }        
        model = LyricsEncoderModel()
        response = model.pre_processing(input_data)        
        
        self.assertEqual('OK', response['status'])        
        self.assertTrue('lyrics' in response)

    def test_registry(self):
        """
        Test NLP model registry
        """
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "universal_sentence_encoder"
        algorithm_object = LyricsEncoderModel()
        algorithm_name = "Universal Sentence Encoder"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "Nitish"
        algorithm_description = "Create sentence embeddings"
        algorithm_code = inspect.getsource(LyricsEncoderModel)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)