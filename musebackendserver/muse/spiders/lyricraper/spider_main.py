import os
import subprocess
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from .lyricraper.spiders import lyricraper, genius
from scrapy.utils.project import get_project_settings

def run_spiders():

    configure_logging()
    runner = CrawlerRunner(get_project_settings())

    filename = './data_storage/songs.txt'
    filename_mxm = 'to_mxm.txt'

    @defer.inlineCallbacks
    def crawl(filename):
        yield runner.crawl(genius.LyricraperSpider, filename=filename)
        yield runner.crawl(lyricraper.LyricraperSpider, filename=filename_mxm)
        reactor.stop()

    crawl(filename)
    reactor.run()
