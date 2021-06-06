import requests
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from muse.settings import SCRAPYD_HOST

SCRAPYD_PROJECT = 'lyricraper'

@api_view(['GET'])
def spider_jobs_status(request):
    """
    List all jobs with their status from scrapyd server
    """
    url = f'{SCRAPYD_HOST}/listjobs.json?project={SCRAPYD_PROJECT}'
    response = requests.get(url)
    return Response(json.loads(response.text))


