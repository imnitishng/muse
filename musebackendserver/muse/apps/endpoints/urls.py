from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import (EndpointViewSet, MLAlgorithmViewSet, 
                    AlgorithmStatusViewSet, NLPRequestViewSet, PredictView,
                    RecommendationsView)

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", AlgorithmStatusViewSet, basename="algorithmstatuses")
router.register(r"mlrequests", NLPRequestViewSet, basename="nlprequests")

urlpatterns = [
    url(r"^api/v1/", include(router.urls)),
    # add predict url
    url(
        r"^api/v1/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"
    ),
    url(
        r"^api/v1/sp_recommedations", RecommendationsView.as_view(), name="spotify_recommendations"
    ),
]