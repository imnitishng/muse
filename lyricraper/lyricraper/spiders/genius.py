import scrapy
import urllib
import csv, os, json
import mysql.connector
import re

class LyricraperSpider(scrapy.Spider):
    # Scraper name
    name = "lyricraper_genius"
    
    def __init__(self, filename='',  **kwargs):
        self.filename = filename
        self.songs = []
        self.start_urls = []

        self.songs_from_file(filename)
        # Parse songs to start urls for scraping
        target_urls = []
        for song in self.songs:
            song = re.sub('\([^\}]*\)', '', song)
            html_encoded = song.replace(' ', '+')            
            search_url = f'https://genius.com/api/search/multi?per_page=5&q={html_encoded}'
            target_urls.append(search_url)

        self.start_urls = target_urls[:]
        super().__init__(**kwargs)

    def songs_from_file(self, filename):
        with open(filename, 'r') as f:
            self.songs = f.readlines()

    def clean_spacing(self, text):
        lis = text.split('\n')
        final = []
        for i in range(len(lis)-1):
            if lis[i]:
                final.append(lis[i])
            if lis[i+1] and lis[i+1][0] == '[':
                final.append('')
        final.append(lis[-1])
        return '\n'.join(final)

    def parse(self, response):
        """
        Extract track names from search and send forward for scraping
        """        
        response_json = json.loads(response.text)
        response_section = response_json.get('response', None).get('sections', None)
        
        if response_section:
            top_results, song_results = response_section[0], response_section[1]                        
            if song_results.get('type', None) == 'song':
                # We consider the first search result
                try:
                    first_hit = song_results.get('hits', None)[0]
                except:
                    # TODO
                    print('aaa')
                track_url = first_hit.get('result', None).get('url', None)

        if track_url:
            search_metadata = response.url.split('=')[-1].replace('+', ' ').split('-')
            artist_name = search_metadata[-1].strip()
            song_name = ''.join(search_metadata[0:len(search_metadata)-1]).strip()

            # First song is all we need, so we follow that link
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

        raw_lyrics = response.xpath('//div[@class="lyrics"]/p').get()                                
        
        # Try the different XPATH for lyrics
        bad_formatting = 0
        if not raw_lyrics:
            raw_lyrics = response.xpath(
                '//div[@class="Lyrics__Container-sc-1ynbvzw-2 jgQsqn"]').getall()
            raw_lyrics = '\n'.join(raw_lyrics)
            bad_formatting = 1

        
        if raw_lyrics:
            # Remove HTML tags from lyrics
            reg_exp_HTML = '<[^>]*>'
            lyrics = re.sub(reg_exp_HTML, '\n', raw_lyrics)
            if bad_formatting:
                lyrics = self.clean_spacing(lyrics)
        else:
            lyrics = "NULL"
        
        data['lyrics'] = lyrics
        data['parent'] = self.filename
        data['type'] = 'lyrics'

        yield data

        