import scrapy
import json
import re
import os
import logging

from apps.endpoints.models import Song, Recommendation

from spiders.lyricraper.utils import defaulters_to_file

class LyricraperSpider(scrapy.Spider):
    # Scraper name
    name = "lyricraper_genius"
    
    def __init__(self, song_ids='', recommendation_id='', **kwargs):
        '''
        Initialize instance variables used to construct URLs and save data
        during the runtime.
        
        Attributes:
            songs: Saves the parsed name of a song used to construct URL for the
                song search result. Format: <Song Name> - <Artist Name>
            song_ids: Saves the UUIDs of the songs for model reference
            urls_to_scrape: Saves constructed search result URLs to scrape
            save_logs: True if the logs will be persisted in the memory in case of
                an exception or missing lyrics. False by default
        '''
        self.songs = []
        self.song_ids = []
        self.urls_to_scrape = []
        self.save_logs = False

        if os.environ.get('SCRAPY_CHECK'):
            self.UserQueryObject = None
            pass
        else:
            self.RecommendationObj = Recommendation.objects.get(pk=recommendation_id)
            self.populate_song_info_from_model(song_ids)
            
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

        Testing:
        @url https://genius.com/api/search/multi?per_page=5&q=Bummerland+-+AJR
        @url https://genius.com/api/search/multi?per_page=5&q=nitishguptaok++-+bbno
        @cb_kwargs {"song_id": 1}
        @returns requests 0 1
        @returns items 0 1
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
        else:
            self.save_logs = True
            logging.error("Something is wrong with website response. Exiting.")
            return
                
        if track_url:
            # First song is all we need, so we follow that link
            yield response.follow(
                track_url, 
                callback=self.parse_lyrics,
                cb_kwargs=dict(song_id=song_id)
            )
        else:
            self.save_logs = True
            # If song not found using this spider then we make an entry for this using pipelines
            yield {
                'type': 'lyrics not found',
                'song_id': song_id
            }

    def parse_lyrics(self, response, song_id):
        """
        Parse song lyrics from a track page
        """
        data = {}

        raw_lyrics = response.xpath('//div[@class="lyrics"]/p').get()                                
        
        # 21:06:21 - OLD lyric class
        # raw_lyrics = response.xpath('//div[@class="Lyrics__Container-sc-1ynbvzw-2 jgQsqn"]').getall()
        # If not found try different XPATH for lyrics
        if not raw_lyrics:
            raw_lyrics = response.xpath('//div[re:test(@class, "Lyrics__Container-sc-1ynbvzw")]').getall()
            raw_lyrics = '\n'.join(raw_lyrics)

        if raw_lyrics:
            # Remove HTML tags and clean lyrics
            reg_exp_HTML = '<[^>]*>'
            lyrics = re.sub(reg_exp_HTML, '\n', raw_lyrics)
            lyrics = self.clean_spacing(lyrics)
        else:
            # The lyrics were found on genius but spider failed to find the DOM element with lyrics correctly
            self.save_logs = True
            lyrics = "scraping_failed"
        
        data['type'] = 'lyrics'
        data['lyrics'] = lyrics
        data['song_id'] = song_id

        yield data

    def populate_song_info_from_model(self, song_ids):
        '''
        Extract songs from django model `Song` based on the `song_ids`
        sent as the spider parameter string.
        '''
        if ',' in song_ids:
            song_ids_list = song_ids.split(',')
        else:
            song_ids_list = [song_ids]

        songs = Song.objects.filter(pk__in=song_ids_list).values_list('id', 'title', 'main_artist')
        for song in songs:
            parsed_songname = song[1] + ' - ' + song[2]
            self.songs.append(parsed_songname)
            self.song_ids.append(song[0].hex)

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
        