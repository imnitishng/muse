import spotipy
import os
import copy

from spotipy.oauth2 import SpotifyClientCredentials
from rest_framework.exceptions import APIException

from apps.endpoints.models import Song, UserRequest
from ..serializers import (SongSerializer, UserRequestSerializer, 
    RecommendationSerializer, UserTrackSelectionSeriializer, SpotifyTrackSelectionSeriializer)

from ..congfigs import CLIENT_ID, CLIENT_SECRET
from ..utils import ignore_invalid_and_save_list, is_duplicate_song_serializer_error


class SpotifyService:
    """
    Object for main query by user
    """

    def __init__(self):
        self.search_term = None
        self.trackInFocusID = None
        self.trackArtistID = None
        self.recommendedTracks = []
        self.recommedation_track_ids = []

        self.searchResultsObj = None
        self.trackInFocusObj = None
        self.trackInFocusFeaturesObj = None
        self.trackArtistObj = None
        self.artistAlbumsObj = []
        self.artistTracksMapObj = {}

        self.client = spotipy.Spotify(
            auth_manager = SpotifyClientCredentials(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET))

    def search_track(self, songname, artist):
        """
        Hit the API to search for a track
        Can work for artist or albums, but
        currently using for tracks.

        Prints the top 20 results.
        """

        self.search_term = songname + ' - ' + artist
        self.searchResultsObj = self.client.search(
            q=self.search_term, limit=20)

    def initialize_track(self, idx):
        """
        Initialize track parameters from backend API call to search and 
        initialize the `idx`th search result be used in all future operations
        """

        self.trackInFocusObj = self.searchResultsObj['tracks']['items'][idx]
        self.trackInFocusID = self.trackInFocusObj['id']        
        self.trackArtistObj = self.trackInFocusObj.get('artists', [None])[0]
        self.trackArtistID = self.trackArtistObj.get('id', None)

    def initialize_track_from_request(self, trackObj):
        """
        Initialize track parameters sent as JSON from frontend app
        to be used in all future operations
        """

        self.trackInFocusObj = trackObj
        self.trackInFocusID = self.trackInFocusObj['id']
        self.trackArtistObj = self.trackInFocusObj.get('artists')[0]
        self.trackArtistID = self.trackArtistObj.get('id')
    
    def get_audio_features(self, idx):
        """
        Reads the search results and track index from 
        search
        Returns audio features for a track
        danceability, energy, loudness, speechiness
        """

        self.trackInFocusFeaturesObj = self.client.audio_features(
            self.trackInFocusID)

    def get_artist_albums(self):
        """
        Get all songs ever released from an artist
        """

        response = self.client.artist_albums(
            self.trackArtistID, album_type='album', limit=50)

        albums_map = {}
        all_albums = response.get('items', None)
        
        # Remove duplicate explicit vs radio edit albums
        for album in all_albums:
            album_name = album.get('name')
            if album_name not in albums_map:
                albums_map[album_name] = 1
                self.artistAlbumsObj.append(album)
            
    def get_all_artist_tracks(self):
        """
        Get all the tracks from artist
        """

        for album in self.artistAlbumsObj:
            response = self.client.album_tracks(album.get('id', None), limit=50)
            songs = response.get('items')
            for song in songs:
                song_name = song.get('name', 'NULL')
                if song_name not in self.artistTracksMapObj:
                    self.artistTracksMapObj[song_name] = song
                    self.recommendedTracks.append(
                        song_name + ' - ' + self.trackArtistObj.get('name')
                    )

    def get_song_recommendations(self, seeds=None):
        """
        Get song recommendations for a song
        """
        if self.trackInFocusID:
            if not seeds:
                response = self.client.recommendations(
                    seed_tracks=[self.trackInFocusID],
                    limit=50,
                    max_speechiness=0.60)
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
            
    def save_recommends_to_file(self):
        filename =  os.getcwd() + '/data_storage/songs.txt'
        with open(filename, 'w') as f:
            for track in self.recommendedTracks:        
                print(track, file=f) 

