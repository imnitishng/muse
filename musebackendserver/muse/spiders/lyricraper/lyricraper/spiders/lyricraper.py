import scrapy
import urllib
import csv, os, json
import mysql.connector
import re

from apps.endpoints.models import Song

class LyricraperSpider(scrapy.Spider):
    # Scraper name
    name = "lyricraper_mxm"
    
    def __init__(self, query_id='',  **kwargs):
        self.filename = filename
        self.songs = []
        self.start_urls = []

        self.songs_from_file(filename)
        self.songs_from_model()
        # Parse songs to start urls for scraping
        target_urls = []
        for song in self.songs:
            html_encoded = urllib.parse.quote(song, safe='')
            search_url = f'https://www.musixmatch.com/search/{html_encoded}'
            target_urls.append(search_url)

        self.start_urls = target_urls[:]
        super().__init__(**kwargs)

    def songs_from_model(self):
        pass

    def songs_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                self.songs = f.readlines()

    def parse(self, response):
        """
        Extract track names from search and send forward for scraping
        """
        track_urls = response.xpath('//div[@class="media-card-text"]/h2/a/@href').getall()
        
        # Build current track data        
        search_metadata = urllib.parse.unquote(response.url.split('/')[-1]).replace('\n', '').split('-')
        artist_name = search_metadata[-1].strip()
        song_name = ''.join(search_metadata[0:len(search_metadata)-1]).strip()

        if track_urls:
            # First song is all we need, so we follow that link
            track_url = response.urljoin(track_urls[0])
            yield response.follow(track_url, 
                callback=self.parse_lyrics,
                cb_kwargs=dict(artist=artist_name, song=song_name))

    def parse_lyrics(self, response, artist, song):
        """
        Parse song lyrics from a track page
        """
        data = {}
        
        data['artist'] = ' '.join(re.findall('([\w]\w+)', artist))
        data['song'] = ' '.join(re.findall('([\w]\w+)', song))
        
        lyrics = response.xpath('//span[@class="lyrics__content__ok"]/text()').getall()
        if not lyrics:
            lyrics = response.xpath('//span[@class="lyrics__content__error"]/text()').getall()                
        
        if lyrics:
            lyrics = '\n'.join(lyrics)
        else:
            lyrics = "NULL"
        
        data['lyrics'] = lyrics
        data['parent'] = self.filename
        data['type'] = 'lyrics'

        yield data

        


