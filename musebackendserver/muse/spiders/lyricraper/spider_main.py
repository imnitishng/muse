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

    query_id = query.id
    retcode = getSongIDsToScrape1(query)

    # @defer.inlineCallbacks
    # def crawl(query):
    #     yield runner.crawl(genius.LyricraperSpider, user_query=query)
        # yield runner.crawl(lyricraper.LyricraperSpider, user_query=query)
        # reactor.stop()

    if retcode:
        crawl(query_id)
        reactor.run()

def crawl(query_id):
