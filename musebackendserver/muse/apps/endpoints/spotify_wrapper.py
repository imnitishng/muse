import spotipy
import random
import os
from spotipy.oauth2 import SpotifyClientCredentials

from .congfigs import CLIENT_ID, CLIENT_SECRET
from ..endpoints.models import Songs

class SpotifySong:
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

        for idx, track in enumerate(self.searchResultsObj['tracks']['items']):
            print(idx, track['name'])

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
        self.trackArtistObj = self.trackInFocusObj.get('artists', [None])[0]
        self.trackArtistID = self.trackArtistObj.get('id', None)
    
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
            
    def get_artist_singles(self):
        # TODO
        pass
    
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

    def get_song_recommendations(self):
        """
        Get song recommendations for a single song
        """

        response = self.client.recommendations(
            seed_tracks=[self.trackInFocusID],
            limit=50,
            max_speechiness=0.60)

        songs = response.get('tracks')
        self.store_songs_to_model(songs)
        return response

    def store_songs_to_model(self, songs):
        for song in songs:
            try:
                spotify_id = song.get('id', None)
                title = song.get('name', 'NULL')
                artists = song.get('artists', 'NULL')
                if not title or not artists:
                    continue
                track_url = song.get('external_urls', None)
                if track_url:
                    track_url = track_url.get('spotify', None)

                preview_url = song.get('preview_url', 'NULL')
                
                artist_info = artists[0].get('href', 'NULL')
                for i in range(len(artists)):
                    artists[i] = artists[i].get('name', 'NULL')

                main_artist = artists[0]

                album = song.get('album', None)
                if album:
                    album_name = album.get('name', 'NULL')
                    album_arts = album.get('images', None)
                    if album_arts:
                        if len(album_arts) > 2:
                            album_art_lg = album_arts[0].get('url')
                            album_art_md = album_arts[1].get('url')
                        else:
                            album_art_lg = album_arts[0].get('url')
                            album_art_md = album_arts[0].get('url')
                else:
                    album_art_lg, album_art_md = None, None
                
                # Save songs to model
                songToSave = Songs(
                    title=title,
                    main_artist=main_artist,
                    artist_info=artist_info,
                    all_artists=artists,
                    album=album_name,
                    spotify_id=spotify_id,
                    album_art_lg=album_art_lg,
                    album_art_md=album_art_md,
                    track_url=track_url,
                    preview_url=preview_url
                )
                songToSave.save()
                
                # Save recomendations to object to return from API
                self.recommendedTracks.append(
                    title + ' - ' + main_artist
                )

                # Save recommended songs for lyrics fetch
                self.recommedation_track_ids.append(songToSave.id)
            except:
                continue

    def save_recommends_to_file(self):
        filename =  os.getcwd() + '/data_storage/songs.txt'
        with open(filename, 'w') as f:
            for track in self.recommendedTracks:        
                print(track, file=f) 

