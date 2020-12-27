import os
import subprocess
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapyd_api import ScrapydAPI

from .lyricraper.spiders import lyricraper, genius
from .lyricraper.spider_utils import getSongIDsToScrape1
from scrapy.utils.project import get_project_settings

from apps.endpoints.models import Songs, SongQueryObject

def run_spiders(query):

    configure_logging()
    runner = CrawlerRunner(get_project_settings())

    query_id = query.query_object.id
    retcode = getSongIDsToScrape1(query)

    if retcode:
        spider_job_id = crawl(query_id)
        return spider_job_id

def crawl(query_id):

    scrapyd = get_spider_instance()
    spider_job_id = scrapyd.schedule('lyricraper', 'lyricraper_genius', user_query_id=query_id)
    return spider_job_id

def get_spider_instance():
    return ScrapydAPI('http://localhost:6800')