from django.conf.urls import url, include

from .views import (PredictView, AccessToken, RecommendationsView, SpidersView, LyricsView)
from apps.nlp.views import ModelView

urlpatterns = [
    url(
        r"api/access_token", AccessToken.as_view(), name="predict"
    ),
    url(
        r"api/sp_recommedations", RecommendationsView.as_view(), name="spotify_recommendations"
    ),
    url(
        r"api/start_fetch", SpidersView.as_view(), name="start_fetch"
    ),
    url(
        r"api/show_lyrics", LyricsView.as_view(), name="show_lyrics"
    ),
    url(
        r"api/get_embeddings", ModelView.as_view(), name="get_embeddings"
    ),
    url(
        r"api/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"
    ),
]