import scrapy
import urllib
import csv, os, json
import mysql.connector
import re

class LyricraperSpider(scrapy.Spider):
    # Scraper name
    name = "lyricraper"
    
    def __init__(self, filename='',  **kwargs):
        self.songs = []
        self.start_urls = []

        self.songs_from_file(filename)
        # Parse songs to start urls for scraping
        target_urls = []
        for song in self.songs:
            html_encoded = urllib.parse.quote(song, safe='')
            search_url = f'https://www.musixmatch.com/search/{html_encoded}'
            target_urls.append(search_url)

        self.start_urls = target_urls[:]
        super().__init__(**kwargs)

    def songs_from_file(self, filename):
        with open(filename, 'r') as f:
            self.songs = f.readlines()

    def parse(self, response):
        """
        Extract track names from search and send forward for scraping
        """
        track_urls = response.xpath('//div[@class="media-card-text"]/h2/a/@href').getall()

        if track_urls:
            # First song is all we need, so we follow that link
            track_url = response.urljoin(track_urls[0])
            yield response.follow(track_url, callback=self.parse_lyrics)

    def parse_lyrics(self, response):
        """
        Parse song lyrics from a track page
        """
        data = {}
        artist, songname = response.url.split('/')[4:]
        
        data['artist'] = ' '.join(re.findall('([\w]\w+)', artist))
        data['song'] = ' '.join(re.findall('([\w]\w+)', songname))
        
        lyrics = response.xpath('//span[@class="lyrics__content__ok"]/text()').getall()
        if not lyrics:
            lyrics = response.xpath('//span[@class="lyrics__content__error"]/text()').getall()        
        lyrics = '\n'.join(lyrics)
        
        data['lyrics'] = lyrics
        data['type'] = 'lyrics'

        yield data

        


