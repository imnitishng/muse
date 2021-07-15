import spotipy
import os
import copy

from spotipy.oauth2 import SpotifyClientCredentials
from rest_framework.exceptions import APIException

from apps.endpoints.models import Song, UserRequest
from ..serializers import (SongSerializer, UserRequestSerializer, 
    RecommendationSerializer, UserTrackSelectionSeriializer, SpotifyTrackSelectionSeriializer)

from muse.settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
from ..utils import ignore_invalid_and_save_list, is_duplicate_song_serializer_error


class SpotifyService:
    """
    Object for main query by user
    """

    def __init__(self):
        self.trackInFocusID = None
        self.trackArtistID = None
        self.trackInFocusObj = None
        self.trackArtistObj = None

        self.client = spotipy.Spotify(
            auth_manager = SpotifyClientCredentials(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET))

    def initialize_track_from_request(self, trackObj):
        """
        Initialize track parameters sent as JSON from frontend app
        to be used in all future operations
        """

        self.trackInFocusObj = trackObj
        self.trackInFocusID = self.trackInFocusObj['id']
        self.trackArtistObj = self.trackInFocusObj.get('artists')[0]
        self.trackArtistID = self.trackArtistObj.get('id')
            
    def getSeedMinMaxValues(self, seeds):
        '''
        The frontend slider for setting track features is very shallow since it only has
        10 possible values so we try to improve that limitation by modifying
        the input seed values to a more detailed request value in order to get 
        better recommendations and minimize outliers because of peculiar values supplied
        by the user.
        
        Eg: 
        A target value for speechiness set from frontend: 0.5
        Updated value for speechiness sent to spotify: min_speechiness = 0.4, max_speechiness = 0.5
        '''
        newSeeds = dict()
        for name, val in seeds.items():
            if name == 'Tempo':
                newSeeds['min_tempo'] = int(val) - 20
                newSeeds['max_tempo'] = int(val) + 20
            elif name == 'Popularity':
                newSeeds['min_popularity'] = int(val) - 5
                newSeeds['max_popularity'] = int(val) + 5
            else:
                newSeeds[f'target_{name.lower()}'] = float(val)
        return newSeeds
    
    def get_song_recommendations(self, seeds=None):
        """
        Get song recommendations for a song
        """
        if self.trackInFocusID:
            if not seeds:
                # If no seeds are sent in the request, i.e. the first request then use default values
                response = self.client.recommendations(
                    seed_tracks=[self.trackInFocusID],
                    limit=50
                )
                return response
            else:
                # If seeds are sent in the request, i.e. user request songs using granularity slider
                SeedValuesDict = self.getSeedMinMaxValues(seeds)
                response = self.client.recommendations(
                    seed_tracks=[self.trackInFocusID],
                    limit=50,
                    **SeedValuesDict
                )
                return response

        else:
            raise APIException("Spotify Service is not initialized. Check `trackObj` in request")

    def save_songs_from_query(self, tracksObj):
        '''
        Save songs from user query to django models and return a list 
        of saved entries
        '''
        if isinstance(tracksObj, dict):
            new, fetched, all = self.store_songs_to_model([tracksObj])
        else:
            new, fetched, all = self.store_songs_to_model(tracksObj)
        return new, fetched, all

    def save_user_query_to_model(self, seeds=None):
        '''
        Save a user query to django models
        '''
        if seeds == None:
            seeds = 'default'

        raw_requestData = {
            'spotifySeeds': seeds
        }
        serializer = UserRequestSerializer(data=raw_requestData)

        if serializer.is_valid(raise_exception=True):
            user_request = serializer.save()
        return user_request
        
    def store_songs_to_model(self, songs):
        '''
        Store relevant information of recommended tracks to Django Models
        and return a list of django models objects for the songs saved successfully
        '''
        saved_songs,fetched_songs = [], []

        try:
            for song in songs:
                # Copy dict to avoid making changes to original data
                tmp_song = copy.deepcopy(song)
                spotify_id = tmp_song.get('id', None)
                title = tmp_song.get('name', None)
                artists = tmp_song.get('artists', None)
                if not title or not artists:
                    continue
                track_url = tmp_song.get('external_urls', None)
                if track_url:
                    track_url = track_url.get('spotify', None)

                preview_url = tmp_song.get('preview_url', None)
                
                artist_info = artists[0].get('href', None)
                for i in range(len(artists)):
                    artists[i] = artists[i].get('name', None)

                main_artist = artists[0]
                if main_artist == None:
                    all_artists = None
                else:
                    all_artists = ', '.join(artists)

                album = tmp_song.get('album', None)
                if album:
                    album_name = album.get('name', None)
                    album_arts = album.get('images', None)
                    if album_arts:
                        if len(album_arts) > 2:
                            album_art_lg = album_arts[0].get('url')
                            album_art_md = album_arts[1].get('url')
                        else:
                            album_art_lg = album_arts[0].get('url')
                            album_art_md = album_arts[0].get('url')
                else:
                    album_name, album_art_lg, album_art_md = None, None, None
                
                # Save songs to model
                raw_songObj = {
                    'title':title,
                    'main_artist':main_artist,
                    'artist_info':artist_info,
                    'all_artists':all_artists,
                    'album':album_name,
                    'spotify_id':spotify_id,
                    'album_art_lg':album_art_lg,
                    'album_art_md':album_art_md,
                    'track_url':track_url,
                    'preview_url':preview_url
                }
            
                serialized_data = SongSerializer(data=raw_songObj)
                if serialized_data.is_valid():
                    saved_data = serialized_data.save()
                    saved_songs.append(saved_data)
                else:
                    if is_duplicate_song_serializer_error(serialized_data.errors):
                        fetched_data = Song.objects.get(spotify_id=spotify_id)
                        fetched_songs.append(fetched_data)
            all_songs = saved_songs + fetched_songs
        except Exception as e:
            raise APIException(str(e))

        return saved_songs, fetched_songs, all_songs

    def save_recommendation_object_to_model(self, user_request_object):
        '''
        Save recommendation object entry to model
        '''
        if isinstance(user_request_object, UserRequest):
            raw_data = {
                'userRequest': user_request_object.id
            }
            serializer = RecommendationSerializer(data=raw_data)
            if serializer.is_valid(raise_exception=True):
                recommendation_obj = serializer.save()
            return recommendation_obj
        else:
            raise(APIException('User request was not initialized properly.'))

    def link_songs_to_parent_objects(self, song_list, parent_object):
        '''
        Save recommendation object entry to model
        '''
        if isinstance(parent_object, UserRequest):
            serializer = UserTrackSelectionSeriializer
        else:
            serializer = SpotifyTrackSelectionSeriializer

        raw_data_list = []
        for song in song_list:
            raw_data = {
                'requestObject': parent_object.id,
                'track': song.id
            }
            raw_data_list.append(raw_data)

        saved_song_object_links = ignore_invalid_and_save_list(data_list=raw_data_list, serializer=serializer)
        return saved_song_object_links
