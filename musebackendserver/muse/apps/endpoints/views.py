from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins


from .models import (Endpoint, MLAlgorithm, 
                            AlgorithmStatus, NLPRequest)
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

