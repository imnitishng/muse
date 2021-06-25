from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH



class Song(models.Model):
    '''
    The Song model saves songs alongwith all the related metadata including lyrics 
    that has been either scraped or queried from API.
    
    Attributes:
        id: PK for the model
        title: Name of song
        artist: Name of artist
        album: Name of album
        spotify_id: Spotify song ID, works as a reference ID for scraper 
        art: Song Art URL
        lyrics: Lyrix
    '''
    title = models.CharField(max_length=2000)
    main_artist = models.CharField(max_length=2000)
    artist_info = models.URLField(max_length=2000, blank=True, null=True)
    all_artists = models.CharField(max_length=2000, blank=True, null=True)
    album = models.CharField(max_length=2000, blank=True, null=True)
    spotify_id = models.CharField(max_length=2000, blank=True, null=True)
    album_art_lg = models.URLField(max_length=2000, blank=True, null=True)
    album_art_md = models.URLField(max_length=2000, blank=True, null=True)
    track_url = models.URLField(max_length=2000, blank=True, null=True)
    preview_url = models.URLField(max_length=2000, blank=True, null=True)
    lyrics = models.CharField(max_length=20000, blank=True, null=True)

    def __str__(self):
        flag = 1 if self.lyrics else 0
        return f'{self.title} by {self.main_artist} | lyrics = {flag}'


class MLAlgorithm(models.Model):
    '''
    The MLAlgorithm represent the ML algorithm object.

    Attributes:
        name: The name of the algorithm.
        description: The short description of how the algorithm works.
        version: The version of the algorithm similar to software versioning.
        owner: The name of the owner.
        created_at: The date when MLAlgorithm was added.
    '''
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class NLPRequest(models.Model):
    '''
    The NLPRequest will keep information about all requests to NLP algorithms.

    Attributes:
        input_data: The input data to algorithm in JSON format.
        full_response: The response of the algorithm.
        response: The response of the algorithm in JSON format.
        feedback: The feedback about the response in JSON format.
        created_at: The date when request was created.
        parent_mlalgorithm: The reference to MLAlgorithm used to compute response.
    '''
    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    request = models.CharField(max_length=10000, blank=True)
    response = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class TracksToID(models.Model):
    '''
    ABSTRACT MODEL
    Stores the mapping of mutiple or single tracks/songs to a single ID
    Each row stores 1 mapping [ID:TrackID] a

    Attributes:
        selection_id: ID for a single query of selected songs
        track_id: Reference to a `Song` Object
    '''
    selectionID = models.UUIDField(unique=False)
    trackID = models.ForeignKey(
        Song,
        db_index=False, 
        null=False, 
        blank=False, 
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        abstract = True


class UserTrackSelection(TracksToID):
    pass


class SpotifyTrackSelection(TracksToID):
    pass


class UserRequest(models.Model):
    '''
    RecommendationsRequest stores all the information from frontend request.

    Attributes:
        selected_tracks: Tracks selected by end user to fetch recommendations for 
        seeds: Spotify music tuning parameters used to filter results
        created_at: Request creation date
    '''
    id = models.UUIDField(
        primary_key=True,
        null=None,
        blank=None
    )
    userSelectedTracks = models.ForeignKey(
        UserTrackSelection,
        db_index=False,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING
    )
    spotifySeeds = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class Recommendation(models.Model):
    '''
    The SongQueryObject will store information about the song selected by user.
    This is the parent based on which all the recommendations will be made.

    Attributes:
        userRequest: Reference to `RecommendationsRequest` Object
        recommendationMap: 
        created_at: The date when object was created
    '''
    id = models.UUIDField(
        primary_key=True,
        null=None,
        blank=None
    )
    userRequest = models.ForeignKey(
        UserRequest,
        db_index=False,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING
    )
    spotifySelectedTracks = models.ForeignKey(
        SpotifyTrackSelection,
        db_index=False,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )


class SongQueryObject(models.Model):
    '''
    The SongQueryObject will keep information about the song selected by user.
    This is the parent based on which all the recommendations will be made.

    Attributes:
        song_name: Name of the song
        artist_name: Name of the song artist
        recommendations: The spotify recommendations for this song in JSON format
        created_at: The date when object was created
    '''
    song_name = models.CharField(max_length=200)
    artist_name = models.CharField(max_length=200)
    recommendations = models.CharField(max_length=10000, blank=True, null=True)
    recommendation_ids = models.CharField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class QueryStatus(models.Model):
    '''
    The QueryStatus will keep track of how which music spiders have to scrape 
    this acts like a realtime dump of song data which will be consumed by 
    spiders to decide and filter what to scrape and what not to scrape.
    '''
    query_object = models.OneToOneField(
        SongQueryObject,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="Query_to_QueryStatus"
    )
    songids_to_process = models.CharField(max_length=10000, blank=True, null=True)
