import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from configs import CLIENT_ID, CLIENT_SECRET

class Song:
    """
    Object for main query by user
    """

    def __init__(self):
        self.search_term = None
        self.trackInFocusID = None
        self.trackArtistID = None

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

    def search_track(self):
        """
        Hit the API to search for a track
        Can work for artist or albums, but
        currently using for tracks.

        Prints the top 20 results.
        """

        print('Search Track: ')
        self.search_term = input()
        print()
        self.searchResultsObj = self.client.search(
            q=self.search_term, limit=20)

        for idx, track in enumerate(
            self.searchResultsObj['tracks']['items']):
            print(idx, track['name'])                

    def initialize_track(self, idx):
        """
        Initialize track parameters to be used in all future operations
        """

        self.trackInFocusObj = self.searchResultsObj['tracks']['items'][idx]
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

    def get_song_recommendations(self):
        """
        Get song recommendations for a single song
        """

        

def main():

    SongEntity = Song()

    SongEntity.search_track()
    SongEntity.initialize_track(0)
    # SongEntity.get_audio_features()
    SongEntity.get_artist_albums()
    SongEntity.get_all_artist_tracks()
    SongEntity.recommendations()

    print('ok boomer')


if __name__ == '__main__':
    main()