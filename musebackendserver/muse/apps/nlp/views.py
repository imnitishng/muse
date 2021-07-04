import json

from rest_framework import views
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from .usencoder.model import UniversalSentenceEncoder
from apps.nlp.serializers import ModelRequestSerializer
from apps.endpoints.models import Recommendation, Song
from apps.endpoints.views.utils import get_tracks_dict_from_recommendation_object
from apps.endpoints.utils import get_lyrics_from_ids_as_list

class ModelView(views.APIView):

    def buildresponse(self, ids, extracted_lyrics, correlation):
        '''
        Build song similarity ranking based on the song queried [1st song]
        '''
        correlation = correlation.get('corr')
        
        # Ranks based on the first song
        main_scores = correlation[0]
        lyrics_dict, scores_dict = {}, {}

        for song_id, score, lyric in zip(ids, main_scores, extracted_lyrics):
            scores_dict[song_id] = score
            lyrics_dict[song_id] = lyric
        
        scores_dict = sorted(scores_dict.items(), key=lambda kv: kv[1], reverse=True)

        rankings = []
        for song_id, score in scores_dict:
            single_rank_response = {
                'id': song_id,
                'score': score,
                'processed_text': lyrics_dict[song_id]
            }
            rankings.append(single_rank_response)

        return rankings
        
    
    def post(self, request, format=None):

        try:
            unsafe_request_data = request.data
            request_serializer = ModelRequestSerializer(data=unsafe_request_data)

            if request_serializer.is_valid(raise_exception=True):
                safe_request_data = request_serializer.data

            recommendation_id = safe_request_data['recommendation_id']
            model_code = safe_request_data['model_code']

            RecommendationObj = Recommendation.objects.get(pk=recommendation_id)
            recommended_tracks_dict = get_tracks_dict_from_recommendation_object(RecommendationObj)
            user_requested_tracks_ids = RecommendationObj.userRequest.selectedTracks.all().values_list('track', flat=True)
            user_requested_tracks_qs = Song.objects.filter(pk__in=user_requested_tracks_ids)
            
            # Perpend user requested songs to top for correlation score
            song_ids, song_lyrics = [], []
            for song in user_requested_tracks_qs:
                song_ids.append(song.id.hex)
                song_lyrics.append(song.lyrics)

            recommended_tracks_list = recommended_tracks_dict['recommended_tracks']
            for song in recommended_tracks_list:
                song_ids.append(song['id'].hex)
                song_lyrics.append(song['lyrics'])

            if model_code == 'use':
                Model = UniversalSentenceEncoder()

            preprocessed_lyrics = Model.pre_processing(song_lyrics)
            payload = {
                'data': preprocessed_lyrics
            }
            # TODO: Send payload one by one based on the memory of the machine
            model_response = Model.get_model_results(payload)
            
            if model_response.status_code == 200:
                ranks = self.buildresponse(song_ids, preprocessed_lyrics, json.loads(model_response.text))
                response = {
                    'status': 'success',
                    'ranks': ranks
                }
            else:
                response = {
                    'status': 'error',
                    'error': 'There was a problem in getting the embeddings.'
                }
            return Response(response)

        except Exception as e:
            raise APIException(str(e))