import json
import requests

from rest_framework import  status
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.decorators import api_view

from muse.settings import SCRAPYD_HOST
from ..models import Recommendation
from ..serializers import RecommendationIDRequestSerializer

from spiders.lyricraper.initiator import run_spiders

SCRAPYD_PROJECT = 'lyricraper'

@api_view(['GET'])
def spider_jobs_status(request):
    """
    List all jobs with their status from scrapyd server
    """
    url = f'{SCRAPYD_HOST}/listjobs.json?project={SCRAPYD_PROJECT}'
    response = requests.get(url)
    return Response(json.loads(response.text))


@api_view(['POST'])
def start_spider_job(request):

    try:
        unsafe_request_data = request.data
        request_serializer = RecommendationIDRequestSerializer(data=unsafe_request_data)

        if request_serializer.is_valid(raise_exception=True):
            safe_request_data = request_serializer.data

        recommendation_id = safe_request_data['recommendation_id']
        RecommendationObj = Recommendation.objects.get(pk=recommendation_id)
        song_to_scrape_ids = RecommendationObj.selectedTracks.all().values_list('track', flat=True)

        SpiderJobID = run_spiders(song_to_scrape_ids, RecommendationObj)

        if SpiderJobID:
            response = {
                'status': 'spider_running',
                'job_id': SpiderJobID,
                'details': 'Started spider to scrape lyrics, query `api/spiders/status` with job_id for status'
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'status': 'spider_not_run',
                'job_id': None,
                'details': 'May happen because data is already scraped or there is an exception while scheduling'
            }
            return Response(response, status=status.HTTP_200_OK)

    except Exception as e:
        raise APIException(str(e))


