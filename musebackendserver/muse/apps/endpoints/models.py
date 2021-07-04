import uuid
from django.db import models


class Song(models.Model):
    '''
    The Song model saves songs alongwith all the related metadata including lyrics 
    that has been either scraped or queried from API.
    
    Attributes:
        id: PK for the model
        title: Name of song
        main_artist: Primary Artist of the track
        artist_info: Info about the artist
        all_artists: All artists for the song
        album: Name of album
        spotify_id: Song ID from Spotify API
        album_art_lg: Large size album art URI
        album_art_md: Medium size album art URI
        track_url: Spotify track play URI 
        preview_url: Spotify short track preview URI 
        lyrics: Lyrix
        created_at: Date of creation
    '''
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=2000)
    main_artist = models.CharField(max_length=2000)
    artist_info = models.URLField(max_length=2000, blank=True, null=True)
    all_artists = models.CharField(max_length=2000, blank=True, null=True)
    album = models.CharField(max_length=2000, blank=True, null=True)
    spotify_id = models.CharField(max_length=2000, unique=True)
    album_art_lg = models.URLField(max_length=2000, blank=True, null=True)
    album_art_md = models.URLField(max_length=2000, blank=True, null=True)
    track_url = models.URLField(max_length=2000, blank=True, null=True)
    preview_url = models.URLField(max_length=2000, blank=True, null=True)
    lyrics = models.CharField(max_length=20000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        flag = 1 if self.lyrics else 0
        return f'{self.title} - {self.main_artist} | lyrics = {flag}'


class UserRequest(models.Model):
    '''
    UserRequest stores information of a user request from frontend request.
    A user request may consist of single or multiple tracks with various parameters 
    for spotify API

    Attributes:
        spotifySeeds: Spotify music tuning parameters used to filter results
        created_at: Request creation date
    '''
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True
    )
    spotifySeeds = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{len(self.selectedTracks.all())} tracks selected on {self.created_at.strftime("%d %b %Y - %H:%M")} as {self.spotifySeeds}'


class Recommendation(models.Model):
    '''
    The Recommendation will store information about the recommended songs returned by Spotify
    The recommendation will be made in response to a `UserRequest` object which is linked below

    Attributes:
        userRequest: Reference to `UserRequest` Object
        created_at: Recommendation creation date
    '''
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
    )
    userRequest = models.ForeignKey(
        UserRequest,
        db_index=False,
        on_delete=models.DO_NOTHING
    )
    emptyLyricsSongIDs = models.CharField(default='', max_length=2000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{len(self.selectedTracks.all())} tracks recommended on {self.created_at.strftime("%d %b %Y - %H:%M")}'


class TracksToID(models.Model):
    '''
    ABSTRACT MODEL
    Stores the mapping of mutiple or single tracks related to different models
    Each row stores 1 mapping [ID:TrackID]

    Attributes:
        selection_id: ID for a single query of selected songs
        track_id: Reference to a `Song` Object
    '''
    track = models.ForeignKey(
        Song,
        db_index=False, 
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        flag = 1 if self.track.lyrics else 0
        return f'{self.track.title} - {self.track.main_artist} | lyrics = {flag}'


class UserTrackSelection(TracksToID):
    '''
    Store trackIDs related to a single query made by User

    Attributes:
        requestObject: Related to parent model `UserRequest`
    '''
    requestObject = models.ForeignKey(
        UserRequest,
        related_name='selectedTracks',
        on_delete=models.CASCADE
    )


class SpotifyTrackSelection(TracksToID):
    '''
    Store trackIDs related to a recommendation returned by spotify

    Attributes:
        requestObject: Related to parent model `Recommendation`
    '''
    requestObject = models.ForeignKey(
        Recommendation,
        related_name='selectedTracks',
        on_delete=models.CASCADE
    )
