from scrapy.utils.log import configure_logging
from scrapyd_api import ScrapydAPI
from scrapyd_client.utils import get_config

from .utils import getSongIDsToScrape1
from muse.settings import SCRAPYD_HOST


def run_spiders(all_song_ids, recommendations_obj):
    configure_logging()
    song_ids = getSongIDsToScrape1(all_song_ids)

    if song_ids:
        song_ids_arg = ','.join(song_ids)
        spider_job_id = crawl(song_ids_arg, recommendations_obj.id.hex)
        return spider_job_id
    else:
        return None

def crawl(song_ids_arg, recommendation_id_hex):
    scrapyd = get_spider_instance()
    spider_job_id = scrapyd.schedule(
        'lyricraper', 
        'lyricraper_genius', 
        song_ids=song_ids_arg, 
        recommendation_id=recommendation_id_hex
    )
    return spider_job_id

def get_spider_instance():
    return ScrapydAPI(SCRAPYD_HOST)
