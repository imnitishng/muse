import scrapy
import urllib
import csv, os, json
import mysql.connector
import re

from apps.endpoints.models import Songs, SongQueryObject, QueryStatus

from ..spider_utils import defaulters_to_file

class LyricraperSpider(scrapy.Spider):
    # Scraper name
    name = "lyricraper_genius"
    
    def __init__(self, user_query='', **kwargs):
        self.songs = []
        self.song_ids = []
        self.urls_to_scrape = []
        
        self.UserQueryObject = user_query
        self.songs_from_model()
        
        # Parse songs to start urls for scraping
        target_urls = []
        for song in self.songs:
            song = re.sub('\([^\}]*\)', '', song)
            html_encoded = song.replace(' ', '+')            
            search_url = f'https://genius.com/api/search/multi?per_page=5&q={html_encoded}'
            target_urls.append(search_url)
        self.urls_to_scrape = target_urls[:]

    def start_requests(self):
        for song_id, url in zip(self.song_ids, self.urls_to_scrape):
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                cb_kwargs=dict(song_id=song_id)
            )

    def parse(self, response, song_id):
        """
        Extract track names from search and send forward for scraping.
                                OR
        Update the query object based on if the search results for the
        particular song is found or not.
        """        
        response_json = json.loads(response.text)
        response_section = response_json.get('response', None).get('sections', None)
        
        if response_section:
            top_results, song_results = response_section[0], response_section[1]                        
            if song_results.get('type', None) == 'song':
                try:
                    # We consider the first search result always
                    first_hit = song_results.get('hits', None)[0]
                    track_url = first_hit.get('result', None).get('url', None)
                except:
                    # Any exception means we never found the searched song
                    track_url = None
                
        if track_url:
            # First song is all we need, so we follow that link
            yield response.follow(
                track_url, 
                callback=self.parse_lyrics,
                cb_kwargs=dict(song_id=song_id)
            )
        else:
            # If song not found then we make an entry for this using pipelines
            yield {
                'type': 'lyrics not found',
                'song_id': song_id,
                'query_obj': self.UserQueryObject
            }

    def parse_lyrics(self, response, song_id):
        """
        Parse song lyrics from a track page
        """
        data = {}

        raw_lyrics = response.xpath('//div[@class="lyrics"]/p').get()                                
        
        # If not found try different XPATH for lyrics
        if not raw_lyrics:
            raw_lyrics = response.xpath(
                '//div[@class="Lyrics__Container-sc-1ynbvzw-2 jgQsqn"]').getall()
            raw_lyrics = '\n'.join(raw_lyrics)
        
        if raw_lyrics:
            # Remove HTML tags and clean lyrics
            reg_exp_HTML = '<[^>]*>'
            lyrics = re.sub(reg_exp_HTML, '\n', raw_lyrics)
            lyrics = self.clean_spacing(lyrics)
        else:
            lyrics = "NULL"
        
        data['type'] = 'lyrics'
        data['lyrics'] = lyrics
        data['song_id'] = song_id
        data['query_id'] = self.UserQueryObject.query_object.id

        yield data

    def songs_from_model(self):
        '''
        Extract songs from django model `Song` based on the query
        recieved by the user.
        '''
        if len(self.UserQueryObject.songids_to_process) > 0:
            requested_songIDs = self.UserQueryObject.songids_to_process.split(',')
            requested_songsDict = Songs.objects.in_bulk(requested_songIDs)
            
            for song_id, song in requested_songsDict.items():
                if song.main_artist and song.title:
                    parsed_songname = song.title + ' - ' + song.main_artist
                    self.songs.append(parsed_songname)
                    self.song_ids.append(song.id)
        else:
            return None

    def songs_from_file(self, filename):
        '''
        Extract list of songs from single line <song_name> <artist>
        format from a file.
        '''
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
        