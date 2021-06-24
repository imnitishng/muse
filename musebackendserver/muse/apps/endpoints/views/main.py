import json
import requests
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from ..models import (MLAlgorithm, NLPRequest,
                    SongQueryObject, QueryStatus, Songs)
from ..spotify_wrapper import SpotifySong
from spiders.lyricraper.spider_main import run_spiders

from ..congfigs import CLIENT_SECRET_BASE64


class AccessToken(views.APIView):

    def get(self, request):
        try:
            spotifyTokenURL = 'https://accounts.spotify.com/api/token'
            headers = {
                'Authorization': f'Basic {CLIENT_SECRET_BASE64}',
                'content-type': 'application/x-www-form-urlencoded'
            }
            payload = {
                'grant_type': 'client_credentials'
            }
            response = requests.post(spotifyTokenURL, headers=headers, data=payload)
            response = json.loads(response.text)
            response = {
                'access_token': response['access_token']
            }

            return Response(response)
        
        except Exception as e:
            raise APIException(str(e))


class RecommendationsView(views.APIView):
    
    def post(self, request, format=None):

        try:
            SongEntity = SpotifySong()
            trackObj = self.request.data.get("spotifyObj", None)
            if trackObj:
                trackObj = json.loads(trackObj)
                SongEntity.initialize_track_from_request(trackObj)
                query_song_name = SongEntity.trackInFocusObj.get('name', None)
                query_artist_name = SongEntity.trackArtistObj.get('name', None)
            else:
                query_song_name = self.request.data.get("song", None)
                query_artist_name = self.request.data.get("artist", None)
                SongEntity.search_track(query_song_name, query_artist_name)
                SongEntity.initialize_track(0)
                                    
            recommendationsObj = SongEntity.get_song_recommendations()

            recommendations = SongEntity.recommendedTracks
            recommendation_ids = str(SongEntity.recommedation_track_ids)[1:-1]
            song_query_object = SongQueryObject(
                song_name = query_song_name,
                artist_name = query_artist_name,
                recommendations = recommendations,
                recommendation_ids = recommendation_ids
            )
            song_query_object.save()
            SongEntity.save_recommends_to_file()

            recommendations_response = {
                "query_id": song_query_object.id,
                "recommendations": SongEntity.recommendedTracks,
                "recommendation_ids": SongEntity.recommedation_track_ids,
                "recommendations_obj": recommendationsObj
            }
            return Response(recommendations_response)

        except Exception as e:
            raise APIException(str(e))


class SpidersView(views.APIView):

    def post(self, request, format=None):

        try:
            query_id = self.request.data.get("query_id", None)
            Query = SongQueryObject.objects.get(id=query_id)
            queried_song_ids = Query.recommendation_ids

            # Clone query info to process and use later
            cloned_query = QueryStatus(
                query_object=Query,
                songids_to_process=queried_song_ids
            )
            cloned_query.save()

            JobID = run_spiders(cloned_query)

            if JobID:
                spider_job_response = {
                    'status': 'Spider Running',
                    'job_id': JobID
                }
            else:
                spider_job_response = {
                    'status': 'Spider failed to run',
                    'job_id': JobID
                }
            return Response(spider_job_response)

        except Exception as e:
            raise APIException(str(e))


class LyricsView(views.APIView):

    def post(self, request, format=None):

        try:
            query_id = self.request.data.get("query_id", None)
            Query = SongQueryObject.objects.get(id=query_id)
            queried_song_ids = Query.recommendation_ids

            song_requested_ids = Query.recommendation_ids.split(',')
            if song_requested_ids:
                QueriedSongsDict = Songs.objects.in_bulk(song_requested_ids)
                response_song_object = []
                for song_id, song in QueriedSongsDict.items():
                    single_song_response = {
                        'title': song.title,
                        'artists': song.all_artists,
                        'lyrics': song.lyrics
                    }
                    response_song_object.append(single_song_response)

                lyrics_response = {
                    'status': 'OK',
                    'query_id': query_id,
                    'songs': response_song_object
                }
                return Response(lyrics_response)
            else:
                fail_response = {
                    'status': 'NOT OK',
                    'query_id': query_id,
                    'songs': 'None found in query'
                }
                return Response(fail_response, status=status.HTTP_400_BAD_REQUEST)
                
        except Exception as e:
            raise APIException(str(e))


class PredictView(views.APIView):
    def post(self, request, endpoint_name, format=None):

        algorithm_status = self.request.query_params.get("status", "production")
        algorithm_version = self.request.query_params.get("version")

        algs = MLAlgorithm.objects.filter(parent_endpoint__name = endpoint_name, status__status = algorithm_status, status__active=True)

        if algorithm_version is not None:
            algs = algs.filter(version = algorithm_version)

        if len(algs) == 0:
            return Response(
                {"status": "Error", "message": "ML algorithm is not available"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if len(algs) != 1 and algorithm_status != "ab_testing":
            return Response(
                {"status": "Error", "message": "ML algorithm selection is ambiguous. Please specify algorithm version."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        alg_index = 0
        if algorithm_status == "ab_testing":
            alg_index = 0 if rand() < 0.5 else 1

        algorithm_object = registry.endpoints[algs[alg_index].id]
        prediction = algorithm_object.pre_processing(request.data)

        prediction = prediction if prediction.get('status', None) == 'OK' else "Error"
        nlp_request = NLPRequest(
            input_data=json.dumps(request.data),
            full_response=prediction,
            response=label,
            feedback="",
            parent_mlalgorithm=algs[alg_index],
        )
        nlp_request.save()

        prediction["request_id"] = nlp_request.id

        return Response(prediction)