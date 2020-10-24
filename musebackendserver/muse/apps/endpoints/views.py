import json
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import views, status
from rest_framework.response import Response

from muse.wsgi import registry
from .spotify_wrapper import Song
from .models import (Endpoint, MLAlgorithm, 
                    SongQueryObject, AlgorithmStatus, NLPRequest)
from .serializers import (EndpointSerializer, MLAlgorithmSerializer, 
                                AlgorithmStatusSerializer, NLPRequestSerializer)


class EndpointViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):    
    serializer_class = EndpointSerializer
    queryset = Endpoint.objects.all()


class MLAlgorithmViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = MLAlgorithmSerializer
    queryset = MLAlgorithm.objects.all()


class AlgorithmStatusViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.CreateModelMixin
):
    serializer_class = AlgorithmStatusSerializer
    queryset = AlgorithmStatus.objects.all()
    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                instance = serializer.save(active=True)
                # set active=False for other statuses
                deactivate_other_statuses(instance)

        except Exception as e:
            raise APIException(str(e))


class NLPRequestViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.UpdateModelMixin
):
    serializer_class = NLPRequestSerializer
    queryset = NLPRequest.objects.all()


def deactivate_other_statuses(instance):
    old_statuses = AlgorithmStatus.objects.filter(
                parent_mlalgorithm = instance.parent_mlalgorithm,
                created_at__lt=instance.created_at,
                active=True)
                
    for i in range(len(old_statuses)):
        old_statuses[i].active = False
    AlgorithmStatus.objects.bulk_update(old_statuses, ["active"])


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


class RecommendationsView(views.APIView):
    
    def post(self, request, format=None):

        query_song_name = self.request.data.get("song", "NULL")
        query_artist_name = self.request.data.get("artist", "NULL")

        SongEntity = Song()
        SongEntity.search_track(query_song_name, query_artist_name)
        SongEntity.initialize_track(0)
        # SongEntity.get_audio_features()
        SongEntity.get_artist_albums()
        SongEntity.get_all_artist_tracks()
        SongEntity.get_song_recommendations()

        recommendations = SongEntity.recommendedTracks        
        song_query_object = SongQueryObject(
            song_name = query_song_name,
            artist_name = query_artist_name,
            recommendations = recommendations
        )
        song_query_object.save()

        recommendations_response = {
            "status": "OK",
            "object_id": song_query_object.id,
            "recommendations": SongEntity.recommendedTracks
        }
        return Response(recommendations_response)


class LyricsView(views.APIView):

    def post(self, request, format=None):
        pass        