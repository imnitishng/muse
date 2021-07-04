import json
import requests

from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from ..models import Recommendation
from ..serializers import SongRequestSerializer, RecommendationIDRequestSerializer

from .utils import get_tracks_dict_from_recommendation_object
from ..services.spotify import SpotifyService
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

        unsafe_request_data = request.data
        request_serializer = SongRequestSerializer(data=unsafe_request_data)

        if request_serializer.is_valid(raise_exception=True):
            safe_request_data = request_serializer.data
        
        try:
            trackObj = safe_request_data.get("spotifyObj")
            spotify_service = SpotifyService()

            # Storing User's requested data
            spotify_service.initialize_track_from_request(trackObj)
            saved_songs, fetched_songs, saved_requested_songs = spotify_service.save_songs_from_query(trackObj)
            user_request = spotify_service.save_user_query_to_model(seeds=None)
            spotify_service.link_songs_to_parent_objects(saved_requested_songs, user_request)
            
            # Storing Spotify's recommended data
            spotifyRecommendationsDict = spotify_service.get_song_recommendations(seeds=None)
            recommendations = spotify_service.save_recommendation_object_to_model(user_request)
            saved_songs, fetched_songs, all_recommended_songs = spotify_service.store_songs_to_model(
                spotifyRecommendationsDict.get('tracks')
            )
            spotify_service.link_songs_to_parent_objects(all_recommended_songs, recommendations)

            response = get_tracks_dict_from_recommendation_object(recommendations)
            return Response(response)

        except Exception as e:
            raise APIException(str(e))


class LyricsView(views.APIView):

    def post(self, request, format=None):

        try:
            unsafe_request_data = request.data
            request_serializer = RecommendationIDRequestSerializer(data=unsafe_request_data)

            if request_serializer.is_valid(raise_exception=True):
                safe_request_data = request_serializer.data

            recommendation_id = safe_request_data['recommendation_id']
            RecommendationObj = Recommendation.objects.get(pk=recommendation_id)
            
            response = get_tracks_dict_from_recommendation_object(RecommendationObj)
            return Response(response)

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