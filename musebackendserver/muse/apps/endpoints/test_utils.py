from .models import SongQueryObject, Songs, QueryStatus


def populate_test_db():
    populate_with_queries()
    populate_with_songs()

def populate_with_queries():
    recommedation_list = ['nursery - bbno$', 'Reborn - KIDS SEE GHOSTS', 'SLOW DANCING IN THE DARK - Joji']
    recommendation_ids = [1, 2, 3]
    song_query_object = SongQueryObject(
        song_name = "cheapskate",
        artist_name = "oliver tree",
        recommendations = recommedation_list,
        recommendation_ids = str(recommendation_ids)[1:-1]
    )
    song_query_object.save()

def populate_with_songs():
    data = [
        {
            "title": "nursery",
            "main_artist": "bbno$",
            "artist_info": "https://api.spotify.com/v1/artists/41X1TR6hrK8Q2ZCpp2EqCz",
            "all_artists": "['bbno$', 'lentra']",
            "album_name": "recess",
            "spotify_id": "2napy7uG4RI74SoyKJVGl5",
            "album_art_lg": "https://i.scdn.co/image/ab67616d0000b2734f33d03da09cfdf70aa804f3",
            "album_art_md": "https://i.scdn.co/image/ab67616d00001e024f33d03da09cfdf70aa804f3",
            "track_url": "https://open.spotify.com/track/2napy7uG4RI74SoyKJVGl5",
            "preview_url": "https://p.scdn.co/mp3-preview/10a838c90b96386b6daa2475178275869e0b8fb9?cid=bd6a887dce7247ecb570fda88090afd8",
            "lyrics": "This is a nursery song ok",
        },
        {
            "title": "Reborn",
            "main_artist": "KIDS SEE GHOSTS",
            "artist_info": "https://api.spotify.com/v1/artists/2hPgGN4uhvXAxiXQBIXOmE",
            "all_artists": "['KIDS SEE GHOSTS']",
            "album_name": "KIDS SEE GHOSTS",
            "spotify_id": "4RVbK6cV0VqWdpCDcx3hiT",
            "album_art_lg": None,
            "album_art_md": "NULL",
            "track_url": "https://open.spotify.com/track/4RVbK6cV0VqWdpCDcx3hiT",
            "preview_url": "None",
            "lyrics": "This is a nursery song ok done",
        },
        {
            "title": "SLOW DANCING IN THE DARK",
            "main_artist": "Joji",
            "artist_info": "https://api.spotify.com/v1/artists/3MZsBdqDrRTJihTHQrO6Dq",
            "all_artists": "['Joji']",
            "album_name": "BALLADS 1",
            "spotify_id": "0rKtyWc8bvkriBthvHKY8d",
            "album_art_lg": "https://i.scdn.co/image/ab67616d0000b27360ba1d6104d0475c7555a6b2",
            "album_art_md": "https://i.scdn.co/image/ab67616d00001e0260ba1d6104d0475c7555a6b2",
            "track_url": "https://open.spotify.com/track/0rKtyWc8bvkriBthvHKY8d",
            "preview_url": "https://p.scdn.co/mp3-preview/483355f39bb264b9828633561ab14a7a48e75270?cid=bd6a887dce7247ecb570fda88090afd8",
            "lyrics": "This is a nursery song yea",
        }
    ]

    for song in data:
        songToSave = Songs(
            title=song['title'],
            main_artist=song['main_artist'],
            artist_info=song['artist_info'],
            all_artists=song['all_artists'],
            album=song['album_name'],
            spotify_id=song['spotify_id'],
            album_art_lg=song['album_art_lg'],
            album_art_md=song['album_art_md'],
            track_url=song['track_url'],
            preview_url=song['preview_url'],
            lyrics=song['lyrics']
        )
        songToSave.save()