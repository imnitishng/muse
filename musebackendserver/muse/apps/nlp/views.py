import json
import requests

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from muse.wsgi import registry

from .usencoder.model import UniversalSentenceEncoder
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
            request_type = self.request.data.get('type', 'full')
            model_name = self.request.data.get('model', 'use')
            song_ids, song_lyrics = [], []

            if request_type == 'full':
                songs_data = self.request.data.get('songs', None)
                
                for song in songs_data:
                    if song:
                        song_ids.append(list(song.keys())[0])
                        song_lyrics.append(list(song.values())[0])
            else:
                song_ids = self.request.data.get('songs', None)
                song_lyrics = get_lyrics_from_ids_as_list(song_ids)


            if model_name == 'use':
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
                    'status': 'OK',
                    'ranks': ranks
                }
            else:
                response = {
                    'error': 'There was a problem in getting the embeddings.',
                    'status': 'NOT OK'
                }
            return Response(response)

        except Exception as e:
            raise APIException(str(e))