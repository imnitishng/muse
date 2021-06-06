from django.conf.urls import url, include

from .views.main import (PredictView, AccessToken, RecommendationsView, SpidersView, LyricsView)
from .views.spider import spider_jobs_status
from apps.nlp.views import ModelView

urlpatterns = [
    # Spotify URLs
    url(
        r"api/spotify/accesstoken", AccessToken.as_view(), name="spotify_accesstoken"
    ),
    url(
        r"api/spotify/recommendations", RecommendationsView.as_view(), name="spotify_recommendations"
    ),

    # Spider URLs
    url(
        r"api/spiders/start", SpidersView.as_view(), name="start_spider"
    ),
    url(
        r"api/spiders/status", spider_jobs_status, name="spider_status"
    ),

    # Model URLs
    url(
        r"api/get_embeddings", ModelView.as_view(), name="get_embeddings"
    ),
    url(
        r"api/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"
    ),

    # Misc URLs
    url(
        r"api/show_lyrics", LyricsView.as_view(), name="show_lyrics"
    ),
]