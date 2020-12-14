from django.db import models


class Endpoint(models.Model):
    '''
    The Endpoint object represents ML API endpoint.

    Attributes:
        name: The name of the endpoint, it will be used in API URL,
        owner: The string with owner name,
        created_at: The date when endpoint was created.
    '''
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)


class MLAlgorithm(models.Model):
    '''
    The MLAlgorithm represent the ML algorithm object.

    Attributes:
        name: The name of the algorithm.
        description: The short description of how the algorithm works.
        code: The code of the algorithm.
        version: The version of the algorithm similar to software versioning.
        owner: The name of the owner.
        created_at: The date when MLAlgorithm was added.
        parent_endpoint: The reference to the Endpoint.
    '''
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)


class NLPObject(models.Model):
    '''
    The NLPObject represent the ML algorithm object.

    Attributes:
        name: The name of the algorithm.
        parent: The name of the parent object of origin (Song).
        created_at: The date when NLPObject was added.
        parent_endpoint: The reference to the Endpoint.
    '''
    name = models.CharField(max_length=128)
    parent = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)


class AlgorithmStatus(models.Model):
    '''
    The AlgorithmStatus represent status of the MLAlgorithm which can change during the time.

    Attributes:
        status: The status of algorithm in the endpoint. Can be: testing, staging, production, ab_testing.
        active: The boolean flag which point to currently active status.
        created_by: The name of creator.
        created_at: The date of status creation.
        parent_mlalgorithm: The reference to corresponding MLAlgorithm.
    '''
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name = "status")


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
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)


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


class Songs(models.Model):
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