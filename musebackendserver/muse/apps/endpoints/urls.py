from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import (EndpointViewSet, MLAlgorithmViewSet, 
                    AlgorithmStatusViewSet, NLPRequestViewSet)

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", AlgorithmStatusViewSet, basename="algorithmstatuses")
router.register(r"mlrequests", NLPRequestViewSet, basename="nlprequests")

urlpatterns = [
    url(r"^api/v1/", include(router.urls)),
]