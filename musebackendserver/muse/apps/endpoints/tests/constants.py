MODEL_SONGS_LIST = [
        {
            "title": "nursery",
            "main_artist": "bbno$",
            "artist_info": "https://api.spotify.com/v1/artists/41X1TR6hrK8Q2ZCpp2EqCz",
            "all_artists": "['bbno$', 'lentra']",
            "album": "recess",
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
            "album": "KIDS SEE GHOSTS",
            "spotify_id": "4RVbK6cV0VqWdpCDcx3hiT",
            "album_art_lg": None,
            "album_art_md": None,
            "track_url": "https://open.spotify.com/track/4RVbK6cV0VqWdpCDcx3hiT",
            "preview_url": None,
            "lyrics": None,
        },
        {
            "title": "SLOW DANCING IN THE DARK",
            "main_artist": "Joji",
            "artist_info": "https://api.spotify.com/v1/artists/3MZsBdqDrRTJihTHQrO6Dq",
            "all_artists": "['Joji']",
            "album": "BALLADS 1",
            "spotify_id": "0rKtyWc8bvkriBthvHKY8d",
            "album_art_lg": "https://i.scdn.co/image/ab67616d0000b27360ba1d6104d0475c7555a6b2",
            "album_art_md": "https://i.scdn.co/image/ab67616d00001e0260ba1d6104d0475c7555a6b2",
            "track_url": "https://open.spotify.com/track/0rKtyWc8bvkriBthvHKY8d",
            "preview_url": "https://p.scdn.co/mp3-preview/483355f39bb264b9828633561ab14a7a48e75270?cid=bd6a887dce7247ecb570fda88090afd8",
            "lyrics": "scraping_failed",
        }
    ]

SEEDS_FOR_RECOMMENDATIONS = {
  'Popularity': 50,
  'Energy': 0.5,
  'Acousticness': 0.5,
  'Tempo': 130,
  'Danceability': 0.5,
  'Instrumentalness': 0.5,
  'Speechiness': 0.5,
}

SPOTIFY_SONG_JSON = '''
    {
        "album": {
            "album_type": "single",
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/6sFIWsNpZYqfjUpaCgueju"
                    },
                    "href": "https://api.spotify.com/v1/artists/6sFIWsNpZYqfjUpaCgueju",
                    "id": "6sFIWsNpZYqfjUpaCgueju",
                    "name": "Carly Rae Jepsen",
                    "type": "artist",
                    "uri": "spotify:artist:6sFIWsNpZYqfjUpaCgueju"
                }
            ],
            "available_markets": [
                "AD",
                "AR",
                "AT",
                "AU",
                "BE",
                "BG",
                "BO",
                "BR",
                "CA",
                "CH",
                "CL",
                "CO",
                "CR",
                "CY",
                "CZ",
                "DE",
                "DK",
                "DO",
                "EC",
                "EE",
                "ES",
                "FI",
                "FR",
                "GB",
                "GR",
                "GT",
                "HK",
                "HN",
                "HU",
                "ID",
                "IE",
                "IL",
                "IS",
                "IT",
                "JP",
                "LI",
                "LT",
                "LU",
                "LV",
                "MC",
                "MT",
                "MX",
                "MY",
                "NI",
                "NL",
                "NO",
                "NZ",
                "PA",
                "PE",
                "PH",
                "PL",
                "PT",
                "PY",
                "RO",
                "SE",
                "SG",
                "SK",
                "SV",
                "TH",
                "TR",
                "TW",
                "US",
                "UY",
                "VN",
                "ZA"
            ],
            "external_urls": {
                "spotify": "https://open.spotify.com/album/0tGPJ0bkWOUmH7MEOR77qc"
            },
            "href": "https://api.spotify.com/v1/albums/0tGPJ0bkWOUmH7MEOR77qc",
            "id": "0tGPJ0bkWOUmH7MEOR77qc",
            "images": [
                {
                    "height": 640,
                    "url": "https://i.scdn.co/image/966ade7a8c43b72faa53822b74a899c675aaafee",
                    "width": 640
                },
                {
                    "height": 300,
                    "url": "https://i.scdn.co/image/107819f5dc557d5d0a4b216781c6ec1b2f3c5ab2",
                    "width": 300
                },
                {
                    "height": 64,
                    "url": "https://i.scdn.co/image/5a73a056d0af707b4119a883d87285feda543fbb",
                    "width": 64
                }
            ],
            "name": "Cut To The Feeling",
            "release_date": "2017-05-26",
            "release_date_precision": "day",
            "type": "album",
            "uri": "spotify:album:0tGPJ0bkWOUmH7MEOR77qc"
        },
        "artists": [
            {
                "external_urls": {
                    "spotify": "https://open.spotify.com/artist/6sFIWsNpZYqfjUpaCgueju"
                },
                "href": "https://api.spotify.com/v1/artists/6sFIWsNpZYqfjUpaCgueju",
                "id": "6sFIWsNpZYqfjUpaCgueju",
                "name": "Carly Rae Jepsen",
                "type": "artist",
                "uri": "spotify:artist:6sFIWsNpZYqfjUpaCgueju"
            }
        ],
        "available_markets": [
            "AD",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "EC",
            "EE",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IS",
            "IT",
            "JP",
            "LI",
            "LT",
            "LU",
            "LV",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "PA",
            "PE",
            "PH",
            "PL",
            "PT",
            "PY",
            "RO",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 207959,
        "explicit": false,
        "external_ids": {
            "isrc": "USUM71703861"
        },
        "external_urls": {
            "spotify": "https://open.spotify.com/track/11dFghVXANMlKmJXsNCbNl"
        },
        "href": "https://api.spotify.com/v1/tracks/11dFghVXANMlKmJXsNCbNl",
        "id": "11dFghVXANMlKmJXsNCbNl",
        "is_local": false,
        "name": "Cut To The Feeling",
        "popularity": 63,
        "preview_url": "https://p.scdn.co/mp3-preview/3eb16018c2a700240e9dfb8817b6f2d041f15eb1?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:11dFghVXANMlKmJXsNCbNl"
    }
    '''

TWO_DUPLICATE_SPOTIFY_SONGS = '''[
    {
        "album": {
            "album_type": "single",
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/6sFIWsNpZYqfjUpaCgueju"
                    },
                    "href": "https://api.spotify.com/v1/artists/6sFIWsNpZYqfjUpaCgueju",
                    "id": "6sFIWsNpZYqfjUpaCgueju",
                    "name": "Carly Rae Jepsen",
                    "type": "artist",
                    "uri": "spotify:artist:6sFIWsNpZYqfjUpaCgueju"
                }
            ],
            "available_markets": [
                "AD",
                "AR",
                "AT",
                "AU",
                "BE",
                "BG",
                "BO",
                "BR",
                "CA",
                "CH",
                "CL",
                "CO",
                "CR",
                "CY",
                "CZ",
                "DE",
                "DK",
                "DO",
                "EC",
                "EE",
                "ES",
                "FI",
                "FR",
                "GB",
                "GR",
                "GT",
                "HK",
                "HN",
                "HU",
                "ID",
                "IE",
                "IL",
                "IS",
                "IT",
                "JP",
                "LI",
                "LT",
                "LU",
                "LV",
                "MC",
                "MT",
                "MX",
                "MY",
                "NI",
                "NL",
                "NO",
                "NZ",
                "PA",
                "PE",
                "PH",
                "PL",
                "PT",
                "PY",
                "RO",
                "SE",
                "SG",
                "SK",
                "SV",
                "TH",
                "TR",
                "TW",
                "US",
                "UY",
                "VN",
                "ZA"
            ],
            "external_urls": {
                "spotify": "https://open.spotify.com/album/0tGPJ0bkWOUmH7MEOR77qc"
            },
            "href": "https://api.spotify.com/v1/albums/0tGPJ0bkWOUmH7MEOR77qc",
            "id": "0tGPJ0bkWOUmH7MEOR77qc",
            "images": [
                {
                    "height": 640,
                    "url": "https://i.scdn.co/image/966ade7a8c43b72faa53822b74a899c675aaafee",
                    "width": 640
                },
                {
                    "height": 300,
                    "url": "https://i.scdn.co/image/107819f5dc557d5d0a4b216781c6ec1b2f3c5ab2",
                    "width": 300
                },
                {
                    "height": 64,
                    "url": "https://i.scdn.co/image/5a73a056d0af707b4119a883d87285feda543fbb",
                    "width": 64
                }
            ],
            "name": "Cut To The Feeling",
            "release_date": "2017-05-26",
            "release_date_precision": "day",
            "type": "album",
            "uri": "spotify:album:0tGPJ0bkWOUmH7MEOR77qc"
        },
        "artists": [
            {
                "external_urls": {
                    "spotify": "https://open.spotify.com/artist/6sFIWsNpZYqfjUpaCgueju"
                },
                "href": "https://api.spotify.com/v1/artists/6sFIWsNpZYqfjUpaCgueju",
                "id": "6sFIWsNpZYqfjUpaCgueju",
                "name": "Carly Rae Jepsen",
                "type": "artist",
                "uri": "spotify:artist:6sFIWsNpZYqfjUpaCgueju"
            }
        ],
        "available_markets": [
            "AD",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "EC",
            "EE",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IS",
            "IT",
            "JP",
            "LI",
            "LT",
            "LU",
            "LV",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "PA",
            "PE",
            "PH",
            "PL",
            "PT",
            "PY",
            "RO",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 207959,
        "explicit": false,
        "external_ids": {
            "isrc": "USUM71703861"
        },
        "external_urls": {
            "spotify": "https://open.spotify.com/track/11dFghVXANMlKmJXsNCbNl"
        },
        "href": "https://api.spotify.com/v1/tracks/11dFghVXANMlKmJXsNCbNl",
        "id": "11dFghVXANMlKmJXsNCbNl",
        "is_local": false,
        "name": "Cut To The Feeling",
        "popularity": 63,
        "preview_url": "https://p.scdn.co/mp3-preview/3eb16018c2a700240e9dfb8817b6f2d041f15eb1?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:11dFghVXANMlKmJXsNCbNl"
    },
    {
        "album": {
            "album_type": "single",
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/6sFIWsNpZYqfjUpaCgueju"
                    },
                    "href": "https://api.spotify.com/v1/artists/6sFIWsNpZYqfjUpaCgueju",
                    "id": "6sFIWsNpZYqfjUpaCgueju",
                    "name": "Carly Rae Jepsen",
                    "type": "artist",
                    "uri": "spotify:artist:6sFIWsNpZYqfjUpaCgueju"
                }
            ],
            "available_markets": [
                "AD",
                "AR",
                "AT",
                "AU",
                "BE",
                "BG",
                "BO",
                "BR",
                "CA",
                "CH",
                "CL",
                "CO",
                "CR",
                "CY",
                "CZ",
                "DE",
                "DK",
                "DO",
                "EC",
                "EE",
                "ES",
                "FI",
                "FR",
                "GB",
                "GR",
                "GT",
                "HK",
                "HN",
                "HU",
                "ID",
                "IE",
                "IL",
                "IS",
                "IT",
                "JP",
                "LI",
                "LT",
                "LU",
                "LV",
                "MC",
                "MT",
                "MX",
                "MY",
                "NI",
                "NL",
                "NO",
                "NZ",
                "PA",
                "PE",
                "PH",
                "PL",
                "PT",
                "PY",
                "RO",
                "SE",
                "SG",
                "SK",
                "SV",
                "TH",
                "TR",
                "TW",
                "US",
                "UY",
                "VN",
                "ZA"
            ],
            "external_urls": {
                "spotify": "https://open.spotify.com/album/0tGPJ0bkWOUmH7MEOR77qc"
            },
            "href": "https://api.spotify.com/v1/albums/0tGPJ0bkWOUmH7MEOR77qc",
            "id": "0tGPJ0bkWOUmH7MEOR77qc",
            "images": [
                {
                    "height": 640,
                    "url": "https://i.scdn.co/image/966ade7a8c43b72faa53822b74a899c675aaafee",
                    "width": 640
                },
                {
                    "height": 300,
                    "url": "https://i.scdn.co/image/107819f5dc557d5d0a4b216781c6ec1b2f3c5ab2",
                    "width": 300
                },
                {
                    "height": 64,
                    "url": "https://i.scdn.co/image/5a73a056d0af707b4119a883d87285feda543fbb",
                    "width": 64
                }
            ],
            "name": "Cut To The Feeling",
            "release_date": "2017-05-26",
            "release_date_precision": "day",
            "type": "album",
            "uri": "spotify:album:0tGPJ0bkWOUmH7MEOR77qc"
        },
        "artists": [
            {
                "external_urls": {
                    "spotify": "https://open.spotify.com/artist/6sFIWsNpZYqfjUpaCgueju"
                },
                "href": "https://api.spotify.com/v1/artists/6sFIWsNpZYqfjUpaCgueju",
                "id": "6sFIWsNpZYqfjUpaCgueju",
                "name": "Carly Rae Jepsen",
                "type": "artist",
                "uri": "spotify:artist:6sFIWsNpZYqfjUpaCgueju"
            }
        ],
        "available_markets": [
            "AD",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "EC",
            "EE",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IS",
            "IT",
            "JP",
            "LI",
            "LT",
            "LU",
            "LV",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "PA",
            "PE",
            "PH",
            "PL",
            "PT",
            "PY",
            "RO",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 207959,
        "explicit": false,
        "external_ids": {
            "isrc": "USUM71703861"
        },
        "external_urls": {
            "spotify": "https://open.spotify.com/track/11dFghVXANMlKmJXsNCbNl"
        },
        "href": "https://api.spotify.com/v1/tracks/11dFghVXANMlKmJXsNCbNl",
        "id": "11dFghVXANMlKmJXsNCbNl",
        "is_local": false,
        "name": "Cut To The Feeling",
        "popularity": 63,
        "preview_url": "https://p.scdn.co/mp3-preview/3eb16018c2a700240e9dfb8817b6f2d041f15eb1?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:11dFghVXANMlKmJXsNCbNl"
    }
  ]
'''

SPOTIFY_RECOMMENDATION_JSON = '''{
  "tracks": [
    {
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/2gsggkzM5R49q6jpPvazou"
          },
          "href": "https://api.spotify.com/v1/artists/2gsggkzM5R49q6jpPvazou",
          "id": "2gsggkzM5R49q6jpPvazou",
          "name": "Jessie J",
          "type": "artist",
          "uri": "spotify:artist:2gsggkzM5R49q6jpPvazou"
        },
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/66CXWjxzNUsdJxJ2JdwvnR"
          },
          "href": "https://api.spotify.com/v1/artists/66CXWjxzNUsdJxJ2JdwvnR",
          "id": "66CXWjxzNUsdJxJ2JdwvnR",
          "name": "Ariana Grande",
          "type": "artist",
          "uri": "spotify:artist:66CXWjxzNUsdJxJ2JdwvnR"
        },
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/0hCNtLu0JehylgoiP8L4Gh"
          },
          "href": "https://api.spotify.com/v1/artists/0hCNtLu0JehylgoiP8L4Gh",
          "id": "0hCNtLu0JehylgoiP8L4Gh",
          "name": "Nicki Minaj",
          "type": "artist",
          "uri": "spotify:artist:0hCNtLu0JehylgoiP8L4Gh"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 199373,
      "explicit": false,
      "external_ids": {
        "isrc": "USUM71409737"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/1rW6UUZRQWW34j4zCQDkfX"
      },
      "href": "https://api.spotify.com/v1/tracks/1rW6UUZRQWW34j4zCQDkfX",
      "id": "1rW6UUZRQWW34j4zCQDkfX",
      "is_local": false,
      "name": "Bang Bang",
      "popularity": 41,
      "preview_url": null,
      "track_number": 4,
      "type": "track",
      "uri": "spotify:track:1rW6UUZRQWW34j4zCQDkfX"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5ivCbtrcD5N4rD337xIb2z"
            },
            "href": "https://api.spotify.com/v1/artists/5ivCbtrcD5N4rD337xIb2z",
            "id": "5ivCbtrcD5N4rD337xIb2z",
            "name": "MisterWives",
            "type": "artist",
            "uri": "spotify:artist:5ivCbtrcD5N4rD337xIb2z"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/3MkcfcWjL0cey5ugIsDe2i"
        },
        "href": "https://api.spotify.com/v1/albums/3MkcfcWjL0cey5ugIsDe2i",
        "id": "3MkcfcWjL0cey5ugIsDe2i",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273aaa9378db13259881e4e3875",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02aaa9378db13259881e4e3875",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851aaa9378db13259881e4e3875",
            "width": 64
          }
        ],
        "name": "Connect The Dots",
        "release_date": "2017-05-19",
        "release_date_precision": "day",
        "total_tracks": 11,
        "type": "album",
        "uri": "spotify:album:3MkcfcWjL0cey5ugIsDe2i"
      },
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 231306,
      "explicit": true,
      "external_ids": {
        "isrc": "USUM71701322"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/2cyfSwcJRd5ikvj34eokdN"
      },
      "href": "https://api.spotify.com/v1/tracks/2cyfSwcJRd5ikvj34eokdN",
      "id": "2cyfSwcJRd5ikvj34eokdN",
      "is_local": false,
      "name": "Coloring Outside The Lines",
      "popularity": 52,
      "preview_url": null,
      "track_number": 8,
      "type": "track",
      "uri": "spotify:track:2cyfSwcJRd5ikvj34eokdN"
    },
    {
      "album": {
        "album_type": "SINGLE",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5p7f24Rk5HkUZsaS3BLG5F"
            },
            "href": "https://api.spotify.com/v1/artists/5p7f24Rk5HkUZsaS3BLG5F",
            "id": "5p7f24Rk5HkUZsaS3BLG5F",
            "name": "Hailee Steinfeld",
            "type": "artist",
            "uri": "spotify:artist:5p7f24Rk5HkUZsaS3BLG5F"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/4w5LxfyoOPHkGJZrco1UT5"
        },
        "href": "https://api.spotify.com/v1/albums/4w5LxfyoOPHkGJZrco1UT5",
        "id": "4w5LxfyoOPHkGJZrco1UT5",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b27339aab3a1fc9e60f4e2bb9b8c",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e0239aab3a1fc9e60f4e2bb9b8c",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d0000485139aab3a1fc9e60f4e2bb9b8c",
            "width": 64
          }
        ],
        "name": "Most Girls",
        "release_date": "2017-04-28",
        "release_date_precision": "day",
        "total_tracks": 1,
        "type": "album",
        "uri": "spotify:album:4w5LxfyoOPHkGJZrco1UT5"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/5p7f24Rk5HkUZsaS3BLG5F"
          },
          "href": "https://api.spotify.com/v1/artists/5p7f24Rk5HkUZsaS3BLG5F",
          "id": "5p7f24Rk5HkUZsaS3BLG5F",
          "name": "Hailee Steinfeld",
          "type": "artist",
          "uri": "spotify:artist:5p7f24Rk5HkUZsaS3BLG5F"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 204400,
      "explicit": false,
      "external_ids": {
        "isrc": "USUM71703935"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/10GJQkjRJcZhGTLagFOC62"
      },
      "href": "https://api.spotify.com/v1/tracks/10GJQkjRJcZhGTLagFOC62",
      "id": "10GJQkjRJcZhGTLagFOC62",
      "is_local": false,
      "name": "Most Girls",
      "popularity": 75,
      "preview_url": null,
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:10GJQkjRJcZhGTLagFOC62"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4m4SfDVbF5wxrwEjDKgi4k"
            },
            "href": "https://api.spotify.com/v1/artists/4m4SfDVbF5wxrwEjDKgi4k",
            "id": "4m4SfDVbF5wxrwEjDKgi4k",
            "name": "Cher Lloyd",
            "type": "artist",
            "uri": "spotify:artist:4m4SfDVbF5wxrwEjDKgi4k"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/0z5qKyh9ys3kk9oLEzgG5l"
        },
        "href": "https://api.spotify.com/v1/albums/0z5qKyh9ys3kk9oLEzgG5l",
        "id": "0z5qKyh9ys3kk9oLEzgG5l",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273ab28d6eea275fe7867e018c3",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02ab28d6eea275fe7867e018c3",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851ab28d6eea275fe7867e018c3",
            "width": 64
          }
        ],
        "name": "Sticks & Stones",
        "release_date": "2011-11-07",
        "release_date_precision": "day",
        "total_tracks": 10,
        "type": "album",
        "uri": "spotify:album:0z5qKyh9ys3kk9oLEzgG5l"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/4m4SfDVbF5wxrwEjDKgi4k"
          },
          "href": "https://api.spotify.com/v1/artists/4m4SfDVbF5wxrwEjDKgi4k",
          "id": "4m4SfDVbF5wxrwEjDKgi4k",
          "name": "Cher Lloyd",
          "type": "artist",
          "uri": "spotify:artist:4m4SfDVbF5wxrwEjDKgi4k"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 214013,
      "explicit": false,
      "external_ids": {
        "isrc": "GBHMU1100104"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/5InWRmnfgjVwQWoXHNBATu"
      },
      "href": "https://api.spotify.com/v1/tracks/5InWRmnfgjVwQWoXHNBATu",
      "id": "5InWRmnfgjVwQWoXHNBATu",
      "is_local": false,
      "name": "Want U Back",
      "popularity": 67,
      "preview_url": "https://p.scdn.co/mp3-preview/9d75eb547252a019927373f70fdacaa293af0caa?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 2,
      "type": "track",
      "uri": "spotify:track:5InWRmnfgjVwQWoXHNBATu"
    },
    {
      "album": {
        "album_type": "SINGLE",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2vGaSKEDFsVPBgcnGxqlBN"
            },
            "href": "https://api.spotify.com/v1/artists/2vGaSKEDFsVPBgcnGxqlBN",
            "id": "2vGaSKEDFsVPBgcnGxqlBN",
            "name": "Alex Newell",
            "type": "artist",
            "uri": "spotify:artist:2vGaSKEDFsVPBgcnGxqlBN"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4ScCswdRlyA23odg9thgIO"
            },
            "href": "https://api.spotify.com/v1/artists/4ScCswdRlyA23odg9thgIO",
            "id": "4ScCswdRlyA23odg9thgIO",
            "name": "Jess Glynne",
            "type": "artist",
            "uri": "spotify:artist:4ScCswdRlyA23odg9thgIO"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1xLOb1CC0N70wA28T7Q5uE"
            },
            "href": "https://api.spotify.com/v1/artists/1xLOb1CC0N70wA28T7Q5uE",
            "id": "1xLOb1CC0N70wA28T7Q5uE",
            "name": "DJ Cassidy",
            "type": "artist",
            "uri": "spotify:artist:1xLOb1CC0N70wA28T7Q5uE"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/3H2mPBmypuqKI2nLeVhLER"
        },
        "href": "https://api.spotify.com/v1/albums/3H2mPBmypuqKI2nLeVhLER",
        "id": "3H2mPBmypuqKI2nLeVhLER",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2735c0d6a1ace5782f888a203e8",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e025c0d6a1ace5782f888a203e8",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048515c0d6a1ace5782f888a203e8",
            "width": 64
          }
        ],
        "name": "Kill The Lights (with Nile Rodgers) [Remixes]",
        "release_date": "2016-04-15",
        "release_date_precision": "day",
        "total_tracks": 4,
        "type": "album",
        "uri": "spotify:album:3H2mPBmypuqKI2nLeVhLER"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/2vGaSKEDFsVPBgcnGxqlBN"
          },
          "href": "https://api.spotify.com/v1/artists/2vGaSKEDFsVPBgcnGxqlBN",
          "id": "2vGaSKEDFsVPBgcnGxqlBN",
          "name": "Alex Newell",
          "type": "artist",
          "uri": "spotify:artist:2vGaSKEDFsVPBgcnGxqlBN"
        },
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/4ScCswdRlyA23odg9thgIO"
          },
          "href": "https://api.spotify.com/v1/artists/4ScCswdRlyA23odg9thgIO",
          "id": "4ScCswdRlyA23odg9thgIO",
          "name": "Jess Glynne",
          "type": "artist",
          "uri": "spotify:artist:4ScCswdRlyA23odg9thgIO"
        },
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/1xLOb1CC0N70wA28T7Q5uE"
          },
          "href": "https://api.spotify.com/v1/artists/1xLOb1CC0N70wA28T7Q5uE",
          "id": "1xLOb1CC0N70wA28T7Q5uE",
          "name": "DJ Cassidy",
          "type": "artist",
          "uri": "spotify:artist:1xLOb1CC0N70wA28T7Q5uE"
        },
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/3yDIp0kaq9EFKe07X1X2rz"
          },
          "href": "https://api.spotify.com/v1/artists/3yDIp0kaq9EFKe07X1X2rz",
          "id": "3yDIp0kaq9EFKe07X1X2rz",
          "name": "Nile Rodgers",
          "type": "artist",
          "uri": "spotify:artist:3yDIp0kaq9EFKe07X1X2rz"
        },
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/4xnMDfgEmXZEEDdITKcGuE"
          },
          "href": "https://api.spotify.com/v1/artists/4xnMDfgEmXZEEDdITKcGuE",
          "id": "4xnMDfgEmXZEEDdITKcGuE",
          "name": "Audien",
          "type": "artist",
          "uri": "spotify:artist:4xnMDfgEmXZEEDdITKcGuE"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 224761,
      "explicit": false,
      "external_ids": {
        "isrc": "USAT21600959"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/4iCKHGl4ij4YMwFrUZLGEQ"
      },
      "href": "https://api.spotify.com/v1/tracks/4iCKHGl4ij4YMwFrUZLGEQ",
      "id": "4iCKHGl4ij4YMwFrUZLGEQ",
      "is_local": false,
      "name": "Kill The Lights (with Nile Rodgers) - Audien Remix",
      "popularity": 62,
      "preview_url": "https://p.scdn.co/mp3-preview/d80ca604db6122c70e47c230c85d49f2c3f97f9a?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:4iCKHGl4ij4YMwFrUZLGEQ"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6T5tfhQCknKG4UnH90qGnz"
            },
            "href": "https://api.spotify.com/v1/artists/6T5tfhQCknKG4UnH90qGnz",
            "id": "6T5tfhQCknKG4UnH90qGnz",
            "name": "DNCE",
            "type": "artist",
            "uri": "spotify:artist:6T5tfhQCknKG4UnH90qGnz"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/3Wv4X8OA65pGpFzBkuUgAh"
        },
        "href": "https://api.spotify.com/v1/albums/3Wv4X8OA65pGpFzBkuUgAh",
        "id": "3Wv4X8OA65pGpFzBkuUgAh",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2738d0a75346badc30c8b845be9",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e028d0a75346badc30c8b845be9",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048518d0a75346badc30c8b845be9",
            "width": 64
          }
        ],
        "name": "DNCE",
        "release_date": "2016-11-18",
        "release_date_precision": "day",
        "total_tracks": 14,
        "type": "album",
        "uri": "spotify:album:3Wv4X8OA65pGpFzBkuUgAh"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/6T5tfhQCknKG4UnH90qGnz"
          },
          "href": "https://api.spotify.com/v1/artists/6T5tfhQCknKG4UnH90qGnz",
          "id": "6T5tfhQCknKG4UnH90qGnz",
          "name": "DNCE",
          "type": "artist",
          "uri": "spotify:artist:6T5tfhQCknKG4UnH90qGnz"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 218973,
      "explicit": false,
      "external_ids": {
        "isrc": "USUM71609364"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/49X8pWDpmFpAITVUaudkcN"
      },
      "href": "https://api.spotify.com/v1/tracks/49X8pWDpmFpAITVUaudkcN",
      "id": "49X8pWDpmFpAITVUaudkcN",
      "is_local": false,
      "name": "Good Day",
      "popularity": 54,
      "preview_url": null,
      "track_number": 7,
      "type": "track",
      "uri": "spotify:track:49X8pWDpmFpAITVUaudkcN"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/5IZLz1qxZ3N2SXLCR9Pv4g"
        },
        "href": "https://api.spotify.com/v1/albums/5IZLz1qxZ3N2SXLCR9Pv4g",
        "id": "5IZLz1qxZ3N2SXLCR9Pv4g",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273306a4ea6e5ead6942fd8818c",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02306a4ea6e5ead6942fd8818c",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851306a4ea6e5ead6942fd8818c",
            "width": 64
          }
        ],
        "name": "Headlines",
        "release_date": "2010-01-01",
        "release_date_precision": "day",
        "total_tracks": 12,
        "type": "album",
        "uri": "spotify:album:5IZLz1qxZ3N2SXLCR9Pv4g"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/15qI5w4XJFLRMwOp2VrlD5"
          },
          "href": "https://api.spotify.com/v1/artists/15qI5w4XJFLRMwOp2VrlD5",
          "id": "15qI5w4XJFLRMwOp2VrlD5",
          "name": "The Saturdays",
          "type": "artist",
          "uri": "spotify:artist:15qI5w4XJFLRMwOp2VrlD5"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 207613,
      "explicit": false,
      "external_ids": {
        "isrc": "GBUM71024215"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/0QVAlchLCx15ZLSoR9Wg1B"
      },
      "href": "https://api.spotify.com/v1/tracks/0QVAlchLCx15ZLSoR9Wg1B",
      "id": "0QVAlchLCx15ZLSoR9Wg1B",
      "is_local": false,
      "name": "Higher",
      "popularity": 58,
      "preview_url": null,
      "track_number": 3,
      "type": "track",
      "uri": "spotify:track:0QVAlchLCx15ZLSoR9Wg1B"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0t3QQl52F463sxGXb1ckhB"
            },
            "href": "https://api.spotify.com/v1/artists/0t3QQl52F463sxGXb1ckhB",
            "id": "0t3QQl52F463sxGXb1ckhB",
            "name": "Betty Who",
            "type": "artist",
            "uri": "spotify:artist:0t3QQl52F463sxGXb1ckhB"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/73AQHzR5yXHtA71tfeX6H2"
        },
        "href": "https://api.spotify.com/v1/albums/73AQHzR5yXHtA71tfeX6H2",
        "id": "73AQHzR5yXHtA71tfeX6H2",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2739cca756edcf7dec94337ad45",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e029cca756edcf7dec94337ad45",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048519cca756edcf7dec94337ad45",
            "width": 64
          }
        ],
        "name": "The Valley",
        "release_date": "2017-03-24",
        "release_date_precision": "day",
        "total_tracks": 13,
        "type": "album",
        "uri": "spotify:album:73AQHzR5yXHtA71tfeX6H2"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/0t3QQl52F463sxGXb1ckhB"
          },
          "href": "https://api.spotify.com/v1/artists/0t3QQl52F463sxGXb1ckhB",
          "id": "0t3QQl52F463sxGXb1ckhB",
          "name": "Betty Who",
          "type": "artist",
          "uri": "spotify:artist:0t3QQl52F463sxGXb1ckhB"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 232053,
      "explicit": true,
      "external_ids": {
        "isrc": "USRC11700169"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/0ZYcjsB94VR5vKrF8pgFvl"
      },
      "href": "https://api.spotify.com/v1/tracks/0ZYcjsB94VR5vKrF8pgFvl",
      "id": "0ZYcjsB94VR5vKrF8pgFvl",
      "is_local": false,
      "name": "You Can Cry Tomorrow",
      "popularity": 35,
      "preview_url": "https://p.scdn.co/mp3-preview/36b96a6bea80ddda1c63a27dd2589655ef92b62a?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 3,
      "type": "track",
      "uri": "spotify:track:0ZYcjsB94VR5vKrF8pgFvl"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5xuNBZoM7z1Vv8IQ6uM0p6"
            },
            "href": "https://api.spotify.com/v1/artists/5xuNBZoM7z1Vv8IQ6uM0p6",
            "id": "5xuNBZoM7z1Vv8IQ6uM0p6",
            "name": "JoJo",
            "type": "artist",
            "uri": "spotify:artist:5xuNBZoM7z1Vv8IQ6uM0p6"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/03B7yRw8C4i7Vuxxjy8RJw"
        },
        "href": "https://api.spotify.com/v1/albums/03B7yRw8C4i7Vuxxjy8RJw",
        "id": "03B7yRw8C4i7Vuxxjy8RJw",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2736f22f9db8574f06adc23ec4e",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e026f22f9db8574f06adc23ec4e",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048516f22f9db8574f06adc23ec4e",
            "width": 64
          }
        ],
        "name": "Mad Love. (Deluxe)",
        "release_date": "2016-10-14",
        "release_date_precision": "day",
        "total_tracks": 15,
        "type": "album",
        "uri": "spotify:album:03B7yRw8C4i7Vuxxjy8RJw"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/5xuNBZoM7z1Vv8IQ6uM0p6"
          },
          "href": "https://api.spotify.com/v1/artists/5xuNBZoM7z1Vv8IQ6uM0p6",
          "id": "5xuNBZoM7z1Vv8IQ6uM0p6",
          "name": "JoJo",
          "type": "artist",
          "uri": "spotify:artist:5xuNBZoM7z1Vv8IQ6uM0p6"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 187440,
      "explicit": false,
      "external_ids": {
        "isrc": "USAT21602574"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/4fcldiaLuLtByymqHk8XDX"
      },
      "href": "https://api.spotify.com/v1/tracks/4fcldiaLuLtByymqHk8XDX",
      "id": "4fcldiaLuLtByymqHk8XDX",
      "is_local": false,
      "name": "Vibe.",
      "popularity": 50,
      "preview_url": "https://p.scdn.co/mp3-preview/3e90cc357297b7b4a1862702fa8c9885c78a692d?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 6,
      "type": "track",
      "uri": "spotify:track:4fcldiaLuLtByymqHk8XDX"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0gBvuNzrFCOVaiyKexoYMH"
            },
            "href": "https://api.spotify.com/v1/artists/0gBvuNzrFCOVaiyKexoYMH",
            "id": "0gBvuNzrFCOVaiyKexoYMH",
            "name": "Todrick Hall",
            "type": "artist",
            "uri": "spotify:artist:0gBvuNzrFCOVaiyKexoYMH"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/7nL2Zecrr7YcvshDt3xGNf"
        },
        "href": "https://api.spotify.com/v1/albums/7nL2Zecrr7YcvshDt3xGNf",
        "id": "7nL2Zecrr7YcvshDt3xGNf",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273b3b1034b958f2c71e813b76b",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02b3b1034b958f2c71e813b76b",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851b3b1034b958f2c71e813b76b",
            "width": 64
          }
        ],
        "name": "Haus Party, Pt. 1",
        "release_date": "2019-05-23",
        "release_date_precision": "day",
        "total_tracks": 7,
        "type": "album",
        "uri": "spotify:album:7nL2Zecrr7YcvshDt3xGNf"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/0gBvuNzrFCOVaiyKexoYMH"
          },
          "href": "https://api.spotify.com/v1/artists/0gBvuNzrFCOVaiyKexoYMH",
          "id": "0gBvuNzrFCOVaiyKexoYMH",
          "name": "Todrick Hall",
          "type": "artist",
          "uri": "spotify:artist:0gBvuNzrFCOVaiyKexoYMH"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 236190,
      "explicit": true,
      "external_ids": {
        "isrc": "USB251977764"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/3dY8y3uZXX0UpDDal2dLhO"
      },
      "href": "https://api.spotify.com/v1/tracks/3dY8y3uZXX0UpDDal2dLhO",
      "id": "3dY8y3uZXX0UpDDal2dLhO",
      "is_local": false,
      "name": "Nails, Hair, Hips, Heels",
      "popularity": 66,
      "preview_url": "https://p.scdn.co/mp3-preview/0fed39af691468fa396ce3a7335b565847792f73?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 6,
      "type": "track",
      "uri": "spotify:track:3dY8y3uZXX0UpDDal2dLhO"
    },
    {
      "album": {
        "album_type": "SINGLE",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2AmfMGi3WZMxqFDHissIAe"
            },
            "href": "https://api.spotify.com/v1/artists/2AmfMGi3WZMxqFDHissIAe",
            "id": "2AmfMGi3WZMxqFDHissIAe",
            "name": "The Aces",
            "type": "artist",
            "uri": "spotify:artist:2AmfMGi3WZMxqFDHissIAe"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/5kZtMQfFg0BMibHRGi6ghX"
        },
        "href": "https://api.spotify.com/v1/albums/5kZtMQfFg0BMibHRGi6ghX",
        "id": "5kZtMQfFg0BMibHRGi6ghX",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b27374e30757ff840d61f91072f2",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e0274e30757ff840d61f91072f2",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d0000485174e30757ff840d61f91072f2",
            "width": 64
          }
        ],
        "name": "I Don't Like Being Honest",
        "release_date": "2017-06-23",
        "release_date_precision": "day",
        "total_tracks": 4,
        "type": "album",
        "uri": "spotify:album:5kZtMQfFg0BMibHRGi6ghX"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/2AmfMGi3WZMxqFDHissIAe"
          },
          "href": "https://api.spotify.com/v1/artists/2AmfMGi3WZMxqFDHissIAe",
          "id": "2AmfMGi3WZMxqFDHissIAe",
          "name": "The Aces",
          "type": "artist",
          "uri": "spotify:artist:2AmfMGi3WZMxqFDHissIAe"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 206466,
      "explicit": false,
      "external_ids": {
        "isrc": "TCACO1639979"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/0x8VeSHmhbRl9EUAdsEx6A"
      },
      "href": "https://api.spotify.com/v1/tracks/0x8VeSHmhbRl9EUAdsEx6A",
      "id": "0x8VeSHmhbRl9EUAdsEx6A",
      "is_local": false,
      "name": "Stuck",
      "popularity": 49,
      "preview_url": "https://p.scdn.co/mp3-preview/0a4b00ae1e9d778b1380b87e04f768eb0d730aa0?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:0x8VeSHmhbRl9EUAdsEx6A"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6sFIWsNpZYqfjUpaCgueju"
            },
            "href": "https://api.spotify.com/v1/artists/6sFIWsNpZYqfjUpaCgueju",
            "id": "6sFIWsNpZYqfjUpaCgueju",
            "name": "Carly Rae Jepsen",
            "type": "artist",
            "uri": "spotify:artist:6sFIWsNpZYqfjUpaCgueju"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/2oj3FG6fos7zAQJxLQGzou"
        },
        "href": "https://api.spotify.com/v1/albums/2oj3FG6fos7zAQJxLQGzou",
        "id": "2oj3FG6fos7zAQJxLQGzou",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2735708b3925c13b1b8d6fac466",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e025708b3925c13b1b8d6fac466",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048515708b3925c13b1b8d6fac466",
            "width": 64
          }
        ],
        "name": "Emotion (Deluxe Expanded Edition)",
        "release_date": "2015",
        "release_date_precision": "year",
        "total_tracks": 17,
        "type": "album",
        "uri": "spotify:album:2oj3FG6fos7zAQJxLQGzou"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/6sFIWsNpZYqfjUpaCgueju"
          },
          "href": "https://api.spotify.com/v1/artists/6sFIWsNpZYqfjUpaCgueju",
          "id": "6sFIWsNpZYqfjUpaCgueju",
          "name": "Carly Rae Jepsen",
          "type": "artist",
          "uri": "spotify:artist:6sFIWsNpZYqfjUpaCgueju"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 251327,
      "explicit": false,
      "external_ids": {
        "isrc": "USUM71507009"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/0FS7B5o3QyvOD8eWjnbLoO"
      },
      "href": "https://api.spotify.com/v1/tracks/0FS7B5o3QyvOD8eWjnbLoO",
      "id": "0FS7B5o3QyvOD8eWjnbLoO",
      "is_local": false,
      "name": "Run Away With Me",
      "popularity": 58,
      "preview_url": null,
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:0FS7B5o3QyvOD8eWjnbLoO"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3WGpXCj9YhhfX11TToZcXP"
            },
            "href": "https://api.spotify.com/v1/artists/3WGpXCj9YhhfX11TToZcXP",
            "id": "3WGpXCj9YhhfX11TToZcXP",
            "name": "Troye Sivan",
            "type": "artist",
            "uri": "spotify:artist:3WGpXCj9YhhfX11TToZcXP"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/3MYJYd73u0SatCnRVvRJ3M"
        },
        "href": "https://api.spotify.com/v1/albums/3MYJYd73u0SatCnRVvRJ3M",
        "id": "3MYJYd73u0SatCnRVvRJ3M",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273aae542061ac42ee04779fb2f",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02aae542061ac42ee04779fb2f",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851aae542061ac42ee04779fb2f",
            "width": 64
          }
        ],
        "name": "Bloom",
        "release_date": "2018-08-31",
        "release_date_precision": "day",
        "total_tracks": 10,
        "type": "album",
        "uri": "spotify:album:3MYJYd73u0SatCnRVvRJ3M"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/3WGpXCj9YhhfX11TToZcXP"
          },
          "href": "https://api.spotify.com/v1/artists/3WGpXCj9YhhfX11TToZcXP",
          "id": "3WGpXCj9YhhfX11TToZcXP",
          "name": "Troye Sivan",
          "type": "artist",
          "uri": "spotify:artist:3WGpXCj9YhhfX11TToZcXP"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 222096,
      "explicit": false,
      "external_ids": {
        "isrc": "AUUM71800411"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/0oTyoTKEKMdF3rXcOLyEfN"
      },
      "href": "https://api.spotify.com/v1/tracks/0oTyoTKEKMdF3rXcOLyEfN",
      "id": "0oTyoTKEKMdF3rXcOLyEfN",
      "is_local": false,
      "name": "Bloom",
      "popularity": 62,
      "preview_url": null,
      "track_number": 2,
      "type": "track",
      "uri": "spotify:track:0oTyoTKEKMdF3rXcOLyEfN"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/163tK9Wjr9P9DmM0AVK7lm"
            },
            "href": "https://api.spotify.com/v1/artists/163tK9Wjr9P9DmM0AVK7lm",
            "id": "163tK9Wjr9P9DmM0AVK7lm",
            "name": "Lorde",
            "type": "artist",
            "uri": "spotify:artist:163tK9Wjr9P9DmM0AVK7lm"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/2B87zXm9bOWvAJdkJBTpzF"
        },
        "href": "https://api.spotify.com/v1/albums/2B87zXm9bOWvAJdkJBTpzF",
        "id": "2B87zXm9bOWvAJdkJBTpzF",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273f8553e18a11209d4becd0336",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02f8553e18a11209d4becd0336",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851f8553e18a11209d4becd0336",
            "width": 64
          }
        ],
        "name": "Melodrama",
        "release_date": "2017-06-16",
        "release_date_precision": "day",
        "total_tracks": 11,
        "type": "album",
        "uri": "spotify:album:2B87zXm9bOWvAJdkJBTpzF"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/163tK9Wjr9P9DmM0AVK7lm"
          },
          "href": "https://api.spotify.com/v1/artists/163tK9Wjr9P9DmM0AVK7lm",
          "id": "163tK9Wjr9P9DmM0AVK7lm",
          "name": "Lorde",
          "type": "artist",
          "uri": "spotify:artist:163tK9Wjr9P9DmM0AVK7lm"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 234652,
      "explicit": false,
      "external_ids": {
        "isrc": "NZUM71700063"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/6ie2Bw3xLj2JcGowOlcMhb"
      },
      "href": "https://api.spotify.com/v1/tracks/6ie2Bw3xLj2JcGowOlcMhb",
      "id": "6ie2Bw3xLj2JcGowOlcMhb",
      "is_local": false,
      "name": "Green Light",
      "popularity": 75,
      "preview_url": null,
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:6ie2Bw3xLj2JcGowOlcMhb"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1Xylc3o4UrD53lo9CvFvVg"
            },
            "href": "https://api.spotify.com/v1/artists/1Xylc3o4UrD53lo9CvFvVg",
            "id": "1Xylc3o4UrD53lo9CvFvVg",
            "name": "Zara Larsson",
            "type": "artist",
            "uri": "spotify:artist:1Xylc3o4UrD53lo9CvFvVg"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/79y7DSLFQH3907u4ysOMGr"
        },
        "href": "https://api.spotify.com/v1/albums/79y7DSLFQH3907u4ysOMGr",
        "id": "79y7DSLFQH3907u4ysOMGr",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273503b16348e47bc3c1c823eba",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02503b16348e47bc3c1c823eba",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851503b16348e47bc3c1c823eba",
            "width": 64
          }
        ],
        "name": "Poster Girl",
        "release_date": "2021-03-05",
        "release_date_precision": "day",
        "total_tracks": 12,
        "type": "album",
        "uri": "spotify:album:79y7DSLFQH3907u4ysOMGr"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/1Xylc3o4UrD53lo9CvFvVg"
          },
          "href": "https://api.spotify.com/v1/artists/1Xylc3o4UrD53lo9CvFvVg",
          "id": "1Xylc3o4UrD53lo9CvFvVg",
          "name": "Zara Larsson",
          "type": "artist",
          "uri": "spotify:artist:1Xylc3o4UrD53lo9CvFvVg"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 190050,
      "explicit": true,
      "external_ids": {
        "isrc": "USSM11807704"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/4nyY8oVjbX2d4qzlpiVM5n"
      },
      "href": "https://api.spotify.com/v1/tracks/4nyY8oVjbX2d4qzlpiVM5n",
      "id": "4nyY8oVjbX2d4qzlpiVM5n",
      "is_local": false,
      "name": "Ruin My Life",
      "popularity": 65,
      "preview_url": "https://p.scdn.co/mp3-preview/7c3d9c8f28c95c0551968b8efe45f6fa162fc403?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 9,
      "type": "track",
      "uri": "spotify:track:4nyY8oVjbX2d4qzlpiVM5n"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3BmGtnKgCSGYIUhmivXKWX"
            },
            "href": "https://api.spotify.com/v1/artists/3BmGtnKgCSGYIUhmivXKWX",
            "id": "3BmGtnKgCSGYIUhmivXKWX",
            "name": "Kelly Clarkson",
            "type": "artist",
            "uri": "spotify:artist:3BmGtnKgCSGYIUhmivXKWX"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/20jYcJane0oI7VoMNoEOJU"
        },
        "href": "https://api.spotify.com/v1/albums/20jYcJane0oI7VoMNoEOJU",
        "id": "20jYcJane0oI7VoMNoEOJU",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273158c72ad0003cb37ca0c9eff",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02158c72ad0003cb37ca0c9eff",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851158c72ad0003cb37ca0c9eff",
            "width": 64
          }
        ],
        "name": "Breakaway",
        "release_date": "2004",
        "release_date_precision": "year",
        "total_tracks": 12,
        "type": "album",
        "uri": "spotify:album:20jYcJane0oI7VoMNoEOJU"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/3BmGtnKgCSGYIUhmivXKWX"
          },
          "href": "https://api.spotify.com/v1/artists/3BmGtnKgCSGYIUhmivXKWX",
          "id": "3BmGtnKgCSGYIUhmivXKWX",
          "name": "Kelly Clarkson",
          "type": "artist",
          "uri": "spotify:artist:3BmGtnKgCSGYIUhmivXKWX"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 188960,
      "explicit": false,
      "external_ids": {
        "isrc": "GBCTA0400231"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/6JY1IdkZGeIcPegKxjSKeb"
      },
      "href": "https://api.spotify.com/v1/tracks/6JY1IdkZGeIcPegKxjSKeb",
      "id": "6JY1IdkZGeIcPegKxjSKeb",
      "is_local": false,
      "name": "Since U Been Gone",
      "popularity": 70,
      "preview_url": "https://p.scdn.co/mp3-preview/476da6381c592fd2d3fd0dbcab6dabb6f234c328?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 2,
      "type": "track",
      "uri": "spotify:track:6JY1IdkZGeIcPegKxjSKeb"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2gsggkzM5R49q6jpPvazou"
            },
            "href": "https://api.spotify.com/v1/artists/2gsggkzM5R49q6jpPvazou",
            "id": "2gsggkzM5R49q6jpPvazou",
            "name": "Jessie J",
            "type": "artist",
            "uri": "spotify:artist:2gsggkzM5R49q6jpPvazou"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/7duJuFUm0IlZW4ppyWSXu5"
        },
        "href": "https://api.spotify.com/v1/albums/7duJuFUm0IlZW4ppyWSXu5",
        "id": "7duJuFUm0IlZW4ppyWSXu5",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273a99212158e6405ba416ef04c",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02a99212158e6405ba416ef04c",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851a99212158e6405ba416ef04c",
            "width": 64
          }
        ],
        "name": "Alive (Deluxe Edition)",
        "release_date": "2013-01-01",
        "release_date_precision": "day",
        "total_tracks": 17,
        "type": "album",
        "uri": "spotify:album:7duJuFUm0IlZW4ppyWSXu5"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/2gsggkzM5R49q6jpPvazou"
          },
          "href": "https://api.spotify.com/v1/artists/2gsggkzM5R49q6jpPvazou",
          "id": "2gsggkzM5R49q6jpPvazou",
          "name": "Jessie J",
          "type": "artist",
          "uri": "spotify:artist:2gsggkzM5R49q6jpPvazou"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 193506,
      "explicit": false,
      "external_ids": {
        "isrc": "USUM71311070"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/60YqDe8UqfRaSFZ6TvPI9u"
      },
      "href": "https://api.spotify.com/v1/tracks/60YqDe8UqfRaSFZ6TvPI9u",
      "id": "60YqDe8UqfRaSFZ6TvPI9u",
      "is_local": false,
      "name": "Sexy Lady",
      "popularity": 60,
      "preview_url": null,
      "track_number": 4,
      "type": "track",
      "uri": "spotify:track:60YqDe8UqfRaSFZ6TvPI9u"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6xdRb2GypJ7DqnWAI2mHGn"
            },
            "href": "https://api.spotify.com/v1/artists/6xdRb2GypJ7DqnWAI2mHGn",
            "id": "6xdRb2GypJ7DqnWAI2mHGn",
            "name": "MUNA",
            "type": "artist",
            "uri": "spotify:artist:6xdRb2GypJ7DqnWAI2mHGn"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/0mfj2MrZptbPw7K5Wo4ikY"
        },
        "href": "https://api.spotify.com/v1/albums/0mfj2MrZptbPw7K5Wo4ikY",
        "id": "0mfj2MrZptbPw7K5Wo4ikY",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273120baf06468dbd74a40582ca",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02120baf06468dbd74a40582ca",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851120baf06468dbd74a40582ca",
            "width": 64
          }
        ],
        "name": "About U",
        "release_date": "2017-02-03",
        "release_date_precision": "day",
        "total_tracks": 12,
        "type": "album",
        "uri": "spotify:album:0mfj2MrZptbPw7K5Wo4ikY"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/6xdRb2GypJ7DqnWAI2mHGn"
          },
          "href": "https://api.spotify.com/v1/artists/6xdRb2GypJ7DqnWAI2mHGn",
          "id": "6xdRb2GypJ7DqnWAI2mHGn",
          "name": "MUNA",
          "type": "artist",
          "uri": "spotify:artist:6xdRb2GypJ7DqnWAI2mHGn"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 272813,
      "explicit": false,
      "external_ids": {
        "isrc": "USRC11602620"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/0bPSRn4crnh5f1JhELPlyL"
      },
      "href": "https://api.spotify.com/v1/tracks/0bPSRn4crnh5f1JhELPlyL",
      "id": "0bPSRn4crnh5f1JhELPlyL",
      "is_local": false,
      "name": "I Know A Place",
      "popularity": 57,
      "preview_url": "https://p.scdn.co/mp3-preview/22cd69ef9886bc7ead93898020e43413ca2234b0?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 3,
      "type": "track",
      "uri": "spotify:track:0bPSRn4crnh5f1JhELPlyL"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6LqNN22kT3074XbTVUrhzX"
            },
            "href": "https://api.spotify.com/v1/artists/6LqNN22kT3074XbTVUrhzX",
            "id": "6LqNN22kT3074XbTVUrhzX",
            "name": "Kesha",
            "type": "artist",
            "uri": "spotify:artist:6LqNN22kT3074XbTVUrhzX"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/1IYVB8NfiRqhdZlTxjspNh"
        },
        "href": "https://api.spotify.com/v1/albums/1IYVB8NfiRqhdZlTxjspNh",
        "id": "1IYVB8NfiRqhdZlTxjspNh",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b27355de63b8aaf464fe8146b4f1",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e0255de63b8aaf464fe8146b4f1",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d0000485155de63b8aaf464fe8146b4f1",
            "width": 64
          }
        ],
        "name": "Rainbow",
        "release_date": "2017-08-11",
        "release_date_precision": "day",
        "total_tracks": 14,
        "type": "album",
        "uri": "spotify:album:1IYVB8NfiRqhdZlTxjspNh"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/6LqNN22kT3074XbTVUrhzX"
          },
          "href": "https://api.spotify.com/v1/artists/6LqNN22kT3074XbTVUrhzX",
          "id": "6LqNN22kT3074XbTVUrhzX",
          "name": "Kesha",
          "type": "artist",
          "uri": "spotify:artist:6LqNN22kT3074XbTVUrhzX"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 217546,
      "explicit": false,
      "external_ids": {
        "isrc": "USRC11701361"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/1g1TeDflB6atAy7HKwrzXu"
      },
      "href": "https://api.spotify.com/v1/tracks/1g1TeDflB6atAy7HKwrzXu",
      "id": "1g1TeDflB6atAy7HKwrzXu",
      "is_local": false,
      "popularity": 54,
      "preview_url": "https://p.scdn.co/mp3-preview/704f8e55b796fa3ebd91cf5eb1c8f9d2967ac5f2?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 6,
      "type": "track",
      "uri": "spotify:track:1g1TeDflB6atAy7HKwrzXu"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6Dd3NScHWwnW6obMFbl1BH"
            },
            "href": "https://api.spotify.com/v1/artists/6Dd3NScHWwnW6obMFbl1BH",
            "id": "6Dd3NScHWwnW6obMFbl1BH",
            "name": "Daya",
            "type": "artist",
            "uri": "spotify:artist:6Dd3NScHWwnW6obMFbl1BH"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/2cE2eOy7alOZHpuelJEV8Q"
        },
        "href": "https://api.spotify.com/v1/albums/2cE2eOy7alOZHpuelJEV8Q",
        "id": "2cE2eOy7alOZHpuelJEV8Q",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273b4c2469ec47edbc937a3070a",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02b4c2469ec47edbc937a3070a",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851b4c2469ec47edbc937a3070a",
            "width": 64
          }
        ],
        "name": "Sit Still, Look Pretty",
        "release_date": "2017-01-06",
        "release_date_precision": "day",
        "total_tracks": 14,
        "type": "album",
        "uri": "spotify:album:2cE2eOy7alOZHpuelJEV8Q"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/6Dd3NScHWwnW6obMFbl1BH"
          },
          "href": "https://api.spotify.com/v1/artists/6Dd3NScHWwnW6obMFbl1BH",
          "id": "6Dd3NScHWwnW6obMFbl1BH",
          "name": "Daya",
          "type": "artist",
          "uri": "spotify:artist:6Dd3NScHWwnW6obMFbl1BH"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 202226,
      "explicit": false,
      "external_ids": {
        "isrc": "QM3EH1500005"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/2DpCdPMg1BADE4HDnxt3Rd"
      },
      "href": "https://api.spotify.com/v1/tracks/2DpCdPMg1BADE4HDnxt3Rd",
      "id": "2DpCdPMg1BADE4HDnxt3Rd",
      "is_local": false,
      "name": "Sit Still, Look Pretty",
      "popularity": 61,
      "preview_url": "https://p.scdn.co/mp3-preview/3988b8743ab763ef4d96aeefaef24e15780fb396?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 8,
      "type": "track",
      "uri": "spotify:track:2DpCdPMg1BADE4HDnxt3Rd"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6UE7nl9mha6s8z0wFQFIZ2"
            },
            "href": "https://api.spotify.com/v1/artists/6UE7nl9mha6s8z0wFQFIZ2",
            "id": "6UE7nl9mha6s8z0wFQFIZ2",
            "name": "Robyn",
            "type": "artist",
            "uri": "spotify:artist:6UE7nl9mha6s8z0wFQFIZ2"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/5OvepfQiCFMCzML6fTgrBW"
        },
        "href": "https://api.spotify.com/v1/albums/5OvepfQiCFMCzML6fTgrBW",
        "id": "5OvepfQiCFMCzML6fTgrBW",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2732dbf3c8a92b1af1942918ad0",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e022dbf3c8a92b1af1942918ad0",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048512dbf3c8a92b1af1942918ad0",
            "width": 64
          }
        ],
        "name": "Robyn Is Here",
        "release_date": "1995-10-13",
        "release_date_precision": "day",
        "total_tracks": 14,
        "type": "album",
        "uri": "spotify:album:5OvepfQiCFMCzML6fTgrBW"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/6UE7nl9mha6s8z0wFQFIZ2"
          },
          "href": "https://api.spotify.com/v1/artists/6UE7nl9mha6s8z0wFQFIZ2",
          "id": "6UE7nl9mha6s8z0wFQFIZ2",
          "name": "Robyn",
          "type": "artist",
          "uri": "spotify:artist:6UE7nl9mha6s8z0wFQFIZ2"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 229226,
      "explicit": false,
      "external_ids": {
        "isrc": "SEBML9707010"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/6SluaPiV04KOaRTOIScoff"
      },
      "href": "https://api.spotify.com/v1/tracks/6SluaPiV04KOaRTOIScoff",
      "id": "6SluaPiV04KOaRTOIScoff",
      "is_local": false,
      "name": "Show Me Love - Radio Version",
      "popularity": 61,
      "preview_url": "https://p.scdn.co/mp3-preview/a0873775085babcfe2d0efdfb987eca7e4c6236d?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 6,
      "type": "track",
      "uri": "spotify:track:6SluaPiV04KOaRTOIScoff"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0t3QQl52F463sxGXb1ckhB"
            },
            "href": "https://api.spotify.com/v1/artists/0t3QQl52F463sxGXb1ckhB",
            "id": "0t3QQl52F463sxGXb1ckhB",
            "name": "Betty Who",
            "type": "artist",
            "uri": "spotify:artist:0t3QQl52F463sxGXb1ckhB"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/73AQHzR5yXHtA71tfeX6H2"
        },
        "href": "https://api.spotify.com/v1/albums/73AQHzR5yXHtA71tfeX6H2",
        "id": "73AQHzR5yXHtA71tfeX6H2",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2739cca756edcf7dec94337ad45",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e029cca756edcf7dec94337ad45",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048519cca756edcf7dec94337ad45",
            "width": 64
          }
        ],
        "name": "The Valley",
        "release_date": "2017-03-24",
        "release_date_precision": "day",
        "total_tracks": 13,
        "type": "album",
        "uri": "spotify:album:73AQHzR5yXHtA71tfeX6H2"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/0t3QQl52F463sxGXb1ckhB"
          },
          "href": "https://api.spotify.com/v1/artists/0t3QQl52F463sxGXb1ckhB",
          "id": "0t3QQl52F463sxGXb1ckhB",
          "name": "Betty Who",
          "type": "artist",
          "uri": "spotify:artist:0t3QQl52F463sxGXb1ckhB"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 223160,
      "explicit": false,
      "external_ids": {
        "isrc": "USRC11601058"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/2i3ziETyx5OGbBRD7Ud92p"
      },
      "href": "https://api.spotify.com/v1/tracks/2i3ziETyx5OGbBRD7Ud92p",
      "id": "2i3ziETyx5OGbBRD7Ud92p",
      "is_local": false,
      "name": "I Love You Always Forever",
      "popularity": 57,
      "preview_url": "https://p.scdn.co/mp3-preview/2b775fdb74806b82452a434e3549c8db69b500ba?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 13,
      "type": "track",
      "uri": "spotify:track:2i3ziETyx5OGbBRD7Ud92p"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1qpR5mURxk3d8f6mww6uKT"
            },
            "href": "https://api.spotify.com/v1/artists/1qpR5mURxk3d8f6mww6uKT",
            "id": "1qpR5mURxk3d8f6mww6uKT",
            "name": "Shura",
            "type": "artist",
            "uri": "spotify:artist:1qpR5mURxk3d8f6mww6uKT"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/2igeHhP9UZ7ko10H1K0DbP"
        },
        "href": "https://api.spotify.com/v1/albums/2igeHhP9UZ7ko10H1K0DbP",
        "id": "2igeHhP9UZ7ko10H1K0DbP",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b27347b93601aed57ab7e31c181a",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e0247b93601aed57ab7e31c181a",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d0000485147b93601aed57ab7e31c181a",
            "width": 64
          }
        ],
        "name": "Nothing's Real",
        "release_date": "2016-07-08",
        "release_date_precision": "day",
        "total_tracks": 13,
        "type": "album",
        "uri": "spotify:album:2igeHhP9UZ7ko10H1K0DbP"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/1qpR5mURxk3d8f6mww6uKT"
          },
          "href": "https://api.spotify.com/v1/artists/1qpR5mURxk3d8f6mww6uKT",
          "id": "1qpR5mURxk3d8f6mww6uKT",
          "name": "Shura",
          "type": "artist",
          "uri": "spotify:artist:1qpR5mURxk3d8f6mww6uKT"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 214754,
      "explicit": false,
      "external_ids": {
        "isrc": "GBUM71600980"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/1Jb8fejyUddXtl2JKAEFmQ"
      },
      "href": "https://api.spotify.com/v1/tracks/1Jb8fejyUddXtl2JKAEFmQ",
      "id": "6p6KdVpfKtTMisH5VfWqsL",
      "is_local": false,
      "name": "What's It Gonna Be?",
      "popularity": 45,
      "preview_url": null,
      "track_number": 3,
      "type": "track",
      "uri": "spotify:track:1Jb8fejyUddXtl2JKAEFmQ"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6CwfuxIqcltXDGjfZsMd9A"
            },
            "href": "https://api.spotify.com/v1/artists/6CwfuxIqcltXDGjfZsMd9A",
            "id": "6CwfuxIqcltXDGjfZsMd9A",
            "name": "MARINA",
            "type": "artist",
            "uri": "spotify:artist:6CwfuxIqcltXDGjfZsMd9A"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/5N1aNUXaHDD7YsjhbCM9JZ"
        },
        "href": "https://api.spotify.com/v1/albums/5N1aNUXaHDD7YsjhbCM9JZ",
        "id": "5N1aNUXaHDD7YsjhbCM9JZ",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b27372513faf9e8385b104f33e85",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e0272513faf9e8385b104f33e85",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d0000485172513faf9e8385b104f33e85",
            "width": 64
          }
        ],
        "name": "Electra Heart (Deluxe)",
        "release_date": "2012-04-30",
        "release_date_precision": "day",
        "total_tracks": 16,
        "type": "album",
        "uri": "spotify:album:5N1aNUXaHDD7YsjhbCM9JZ"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/6CwfuxIqcltXDGjfZsMd9A"
          },
          "href": "https://api.spotify.com/v1/artists/6CwfuxIqcltXDGjfZsMd9A",
          "id": "6CwfuxIqcltXDGjfZsMd9A",
          "name": "MARINA",
          "type": "artist",
          "uri": "spotify:artist:6CwfuxIqcltXDGjfZsMd9A"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 221493,
      "explicit": false,
      "external_ids": {
        "isrc": "GBFFS1200077"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/2Ow4Pmi0VOOLvbmJ8V70qo"
      },
      "href": "https://api.spotify.com/v1/tracks/2Ow4Pmi0VOOLvbmJ8V70qo",
      "id": "2Ow4Pmi0VOOLvbmJ8V70qo",
      "is_local": false,
      "name": "How to Be a Heartbreaker",
      "popularity": 70,
      "preview_url": "https://p.scdn.co/mp3-preview/3f4e3f70e4eaa15ec8397dee9b509bcd702a5805?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 12,
      "type": "track",
      "uri": "spotify:track:2Ow4Pmi0VOOLvbmJ8V70qo"
    },
    {
      "album": {
        "album_type": "SINGLE",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6Paz0vXJJ9bCPf0fEm3qzg"
            },
            "href": "https://api.spotify.com/v1/artists/6Paz0vXJJ9bCPf0fEm3qzg",
            "id": "6Paz0vXJJ9bCPf0fEm3qzg",
            "name": "Dagny",
            "type": "artist",
            "uri": "spotify:artist:6Paz0vXJJ9bCPf0fEm3qzg"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/5aajmZb0CP87NOngM8N6At"
        },
        "href": "https://api.spotify.com/v1/albums/5aajmZb0CP87NOngM8N6At",
        "id": "5aajmZb0CP87NOngM8N6At",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2738e984fbcb01051d15ad5297d",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e028e984fbcb01051d15ad5297d",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048518e984fbcb01051d15ad5297d",
            "width": 64
          }
        ],
        "name": "More More More",
        "release_date": "2017-09-08",
        "release_date_precision": "day",
        "total_tracks": 1,
        "type": "album",
        "uri": "spotify:album:5aajmZb0CP87NOngM8N6At"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/6Paz0vXJJ9bCPf0fEm3qzg"
          },
          "href": "https://api.spotify.com/v1/artists/6Paz0vXJJ9bCPf0fEm3qzg",
          "id": "6Paz0vXJJ9bCPf0fEm3qzg",
          "name": "Dagny",
          "type": "artist",
          "uri": "spotify:artist:6Paz0vXJJ9bCPf0fEm3qzg"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 199226,
      "explicit": false,
      "external_ids": {
        "isrc": "USUM71708956"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/7i7y9mbMd15VpXOtWrORPv"
      },
      "href": "https://api.spotify.com/v1/tracks/7i7y9mbMd15VpXOtWrORPv",
      "id": "7i7y9mbMd15VpXOtWrORPv",
      "is_local": false,
      "name": "More More More",
      "popularity": 32,
      "preview_url": null,
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:7i7y9mbMd15VpXOtWrORPv"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6sFIWsNpZYqfjUpaCgueju"
            },
            "href": "https://api.spotify.com/v1/artists/6sFIWsNpZYqfjUpaCgueju",
            "id": "6sFIWsNpZYqfjUpaCgueju",
            "name": "Carly Rae Jepsen",
            "type": "artist",
            "uri": "spotify:artist:6sFIWsNpZYqfjUpaCgueju"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/2oj3FG6fos7zAQJxLQGzou"
        },
        "href": "https://api.spotify.com/v1/albums/2oj3FG6fos7zAQJxLQGzou",
        "id": "2oj3FG6fos7zAQJxLQGzou",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2735708b3925c13b1b8d6fac466",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e025708b3925c13b1b8d6fac466",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048515708b3925c13b1b8d6fac466",
            "width": 64
          }
        ],
        "name": "Emotion (Deluxe Expanded Edition)",
        "release_date": "2015",
        "release_date_precision": "year",
        "total_tracks": 17,
        "type": "album",
        "uri": "spotify:album:2oj3FG6fos7zAQJxLQGzou"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/6sFIWsNpZYqfjUpaCgueju"
          },
          "href": "https://api.spotify.com/v1/artists/6sFIWsNpZYqfjUpaCgueju",
          "id": "6sFIWsNpZYqfjUpaCgueju",
          "name": "Carly Rae Jepsen",
          "type": "artist",
          "uri": "spotify:artist:6sFIWsNpZYqfjUpaCgueju"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 202232,
      "explicit": false,
      "external_ids": {
        "isrc": "USUM71507025"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/6br39bRzXUNsbJtIMnQbXb"
      },
      "href": "https://api.spotify.com/v1/tracks/6br39bRzXUNsbJtIMnQbXb",
      "id": "6br39bRzXUNsbJtIMnQbXb",
      "is_local": false,
      "name": "Gimmie Love",
      "popularity": 46,
      "preview_url": null,
      "track_number": 4,
      "type": "track",
      "uri": "spotify:track:6br39bRzXUNsbJtIMnQbXb"
    },
    {
      "album": {
        "album_type": "SINGLE",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2vm8GdHyrJh2O2MfbQFYG0"
            },
            "href": "https://api.spotify.com/v1/artists/2vm8GdHyrJh2O2MfbQFYG0",
            "id": "2vm8GdHyrJh2O2MfbQFYG0",
            "name": "Ingrid Michaelson",
            "type": "artist",
            "uri": "spotify:artist:2vm8GdHyrJh2O2MfbQFYG0"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/6xdZ62j7AOvgF40lqK4w50"
        },
        "href": "https://api.spotify.com/v1/albums/6xdZ62j7AOvgF40lqK4w50",
        "id": "6xdZ62j7AOvgF40lqK4w50",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273a17b1a23000ce90aabf63d17",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02a17b1a23000ce90aabf63d17",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851a17b1a23000ce90aabf63d17",
            "width": 64
          }
        ],
        "name": "Celebrate",
        "release_date": "2016-05-08",
        "release_date_precision": "day",
        "total_tracks": 1,
        "type": "album",
        "uri": "spotify:album:6xdZ62j7AOvgF40lqK4w50"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/2vm8GdHyrJh2O2MfbQFYG0"
          },
          "href": "https://api.spotify.com/v1/artists/2vm8GdHyrJh2O2MfbQFYG0",
          "id": "2vm8GdHyrJh2O2MfbQFYG0",
          "name": "Ingrid Michaelson",
          "type": "artist",
          "uri": "spotify:artist:2vm8GdHyrJh2O2MfbQFYG0"
        },
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/6s22t5Y3prQHyaHWUN1R1C"
          },
          "href": "https://api.spotify.com/v1/artists/6s22t5Y3prQHyaHWUN1R1C",
          "id": "6s22t5Y3prQHyaHWUN1R1C",
          "name": "AJR",
          "type": "artist",
          "uri": "spotify:artist:6s22t5Y3prQHyaHWUN1R1C"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 197720,
      "explicit": false,
      "external_ids": {
        "isrc": "USVT31800004"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/0iF2k99DJgFbPmsUQUFbtm"
      },
      "href": "https://api.spotify.com/v1/tracks/0iF2k99DJgFbPmsUQUFbtm",
      "id": "0iF2k99DJgFbPmsUQUFbtm",
      "is_local": false,
      "name": "Celebrate",
      "popularity": 43,
      "preview_url": null,
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:0iF2k99DJgFbPmsUQUFbtm"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6DIS6PRrLS3wbnZsf7vYic"
            },
            "href": "https://api.spotify.com/v1/artists/6DIS6PRrLS3wbnZsf7vYic",
            "id": "6DIS6PRrLS3wbnZsf7vYic",
            "name": "WALK THE MOON",
            "type": "artist",
            "uri": "spotify:artist:6DIS6PRrLS3wbnZsf7vYic"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/3mNoFlD1wsoXfkljfFzExT"
        },
        "href": "https://api.spotify.com/v1/albums/3mNoFlD1wsoXfkljfFzExT",
        "id": "3mNoFlD1wsoXfkljfFzExT",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b27343294cfa2688055c9d821bf3",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e0243294cfa2688055c9d821bf3",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d0000485143294cfa2688055c9d821bf3",
            "width": 64
          }
        ],
        "name": "TALKING IS HARD",
        "release_date": "2014-12-02",
        "release_date_precision": "day",
        "total_tracks": 12,
        "type": "album",
        "uri": "spotify:album:3mNoFlD1wsoXfkljfFzExT"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/6DIS6PRrLS3wbnZsf7vYic"
          },
          "href": "https://api.spotify.com/v1/artists/6DIS6PRrLS3wbnZsf7vYic",
          "id": "6DIS6PRrLS3wbnZsf7vYic",
          "name": "WALK THE MOON",
          "type": "artist",
          "uri": "spotify:artist:6DIS6PRrLS3wbnZsf7vYic"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 175906,
      "explicit": false,
      "external_ids": {
        "isrc": "USRC11402587"
      },
      "id": "76EeScTnI2sCjDY0SfEoSb",
      "is_local": false,
      "name": "Work This Body",
      "popularity": 59,
      "track_number": 8,
      "type": "track",
      "uri": "spotify:track:76EeScTnI2sCjDY0SfEoSb"
    },
    {
      "album": {
        "album_type": "SINGLE",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3Yl4nkmEa8BSuGWbwhdLDq"
            },
            "href": "https://api.spotify.com/v1/artists/3Yl4nkmEa8BSuGWbwhdLDq",
            "id": "3Yl4nkmEa8BSuGWbwhdLDq",
            "name": "G.R.L.",
            "type": "artist",
            "uri": "spotify:artist:3Yl4nkmEa8BSuGWbwhdLDq"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/6cvanscbjwTlkleedLkWhC"
        },
        "href": "https://api.spotify.com/v1/albums/6cvanscbjwTlkleedLkWhC",
        "id": "6cvanscbjwTlkleedLkWhC",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b27363fae1618148f297ab8380f4",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e0263fae1618148f297ab8380f4",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d0000485163fae1618148f297ab8380f4",
            "width": 64
          }
        ],
        "name": "Ugly Heart",
        "release_date": "2014-06-03",
        "release_date_precision": "day",
        "total_tracks": 1,
        "type": "album",
        "uri": "spotify:album:6cvanscbjwTlkleedLkWhC"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/3Yl4nkmEa8BSuGWbwhdLDq"
          },
          "href": "https://api.spotify.com/v1/artists/3Yl4nkmEa8BSuGWbwhdLDq",
          "id": "3Yl4nkmEa8BSuGWbwhdLDq",
          "name": "G.R.L.",
          "type": "artist",
          "uri": "spotify:artist:3Yl4nkmEa8BSuGWbwhdLDq"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 199580,
      "explicit": false,
      "external_ids": {
        "isrc": "USRC11400627"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/1Vv0MPcooEoQzVZYfKMgKW"
      },
      "href": "https://api.spotify.com/v1/tracks/1Vv0MPcooEoQzVZYfKMgKW",
      "id": "1Vv0MPcooEoQzVZYfKMgKW",
      "is_local": false,
      "name": "Ugly Heart",
      "popularity": 68,
      "preview_url": "https://p.scdn.co/mp3-preview/b740a547811091b4140e961feea439cc366dd40d?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:1Vv0MPcooEoQzVZYfKMgKW"
    },
    {
      "album": {
        "album_type": "SINGLE",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5CCwRZC6euC8Odo6y9X8jr"
            },
            "href": "https://api.spotify.com/v1/artists/5CCwRZC6euC8Odo6y9X8jr",
            "id": "5CCwRZC6euC8Odo6y9X8jr",
            "name": "Rita Ora",
            "type": "artist",
            "uri": "spotify:artist:5CCwRZC6euC8Odo6y9X8jr"
          }
        ],
        "available_markets": [],
        "href": "https://api.spotify.com/v1/albums/415fhs8Ft2VMFY0rWLK4BD",
        "id": "415fhs8Ft2VMFY0rWLK4BD",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273bd6c207be091d0b107405b93",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02bd6c207be091d0b107405b93",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851bd6c207be091d0b107405b93",
            "width": 64
          }
        ],
        "release_date": "2014-03-31",
        "release_date_precision": "day",
        "total_tracks": 1,
        "type": "album",
        "uri": "spotify:album:415fhs8Ft2VMFY0rWLK4BD"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/5CCwRZC6euC8Odo6y9X8jr"
          },
          "href": "https://api.spotify.com/v1/artists/5CCwRZC6euC8Odo6y9X8jr",
          "id": "5CCwRZC6euC8Odo6y9X8jr",
          "type": "artist",
          "uri": "spotify:artist:5CCwRZC6euC8Odo6y9X8jr"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 203466,
      "explicit": false,
      "external_ids": {
        "isrc": "USQX91400359"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/2ia7iiEtpiOL2ZVuWxBZGB"
      },
      "href": "https://api.spotify.com/v1/tracks/2ia7iiEtpiOL2ZVuWxBZGB",
      "id": "2ia7iiEtpiOL2ZVuWxBZGB",
      "is_local": false,
      "name": "I Will Never Let You Down",
      "popularity": 66,
      "preview_url": "https://p.scdn.co/mp3-preview/70d65e1fdbf17773c1b9ea73b35785deb6a659a9?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:2ia7iiEtpiOL2ZVuWxBZGB"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3BmGtnKgCSGYIUhmivXKWX"
            },
            "href": "https://api.spotify.com/v1/artists/3BmGtnKgCSGYIUhmivXKWX",
            "id": "3BmGtnKgCSGYIUhmivXKWX",
            "name": "Kelly Clarkson",
            "type": "artist",
            "uri": "spotify:artist:3BmGtnKgCSGYIUhmivXKWX"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/6GBu7GU6dztLYlZuUHiwA2"
        },
        "href": "https://api.spotify.com/v1/albums/6GBu7GU6dztLYlZuUHiwA2",
        "id": "6GBu7GU6dztLYlZuUHiwA2",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2731b808f1c7fff4f3e81f79523",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e021b808f1c7fff4f3e81f79523",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048511b808f1c7fff4f3e81f79523",
            "width": 64
          }
        ],
        "name": "Meaning of Life",
        "release_date": "2017-10-27",
        "release_date_precision": "day",
        "total_tracks": 14,
        "type": "album",
        "uri": "spotify:album:6GBu7GU6dztLYlZuUHiwA2"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/3BmGtnKgCSGYIUhmivXKWX"
          },
          "href": "https://api.spotify.com/v1/artists/3BmGtnKgCSGYIUhmivXKWX",
          "id": "3BmGtnKgCSGYIUhmivXKWX",
          "name": "Kelly Clarkson",
          "type": "artist",
          "uri": "spotify:artist:3BmGtnKgCSGYIUhmivXKWX"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 172426,
      "explicit": false,
      "external_ids": {
        "isrc": "USAT21703569"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/16QN8cBubEq706vNtPpOME"
      },
      "href": "https://api.spotify.com/v1/tracks/16QN8cBubEq706vNtPpOME",
      "id": "16QN8cBubEq706vNtPpOME",
      "is_local": false,
      "name": "Love So Soft",
      "popularity": 59,
      "preview_url": "https://p.scdn.co/mp3-preview/052c920e5102903914079dd5fc03c4601ba34659?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 2,
      "type": "track",
      "uri": "spotify:track:16QN8cBubEq706vNtPpOME"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6LqNN22kT3074XbTVUrhzX"
            },
            "href": "https://api.spotify.com/v1/artists/6LqNN22kT3074XbTVUrhzX",
            "id": "6LqNN22kT3074XbTVUrhzX",
            "name": "Kesha",
            "type": "artist",
            "uri": "spotify:artist:6LqNN22kT3074XbTVUrhzX"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/1IYVB8NfiRqhdZlTxjspNh"
        },
        "href": "https://api.spotify.com/v1/albums/1IYVB8NfiRqhdZlTxjspNh",
        "id": "1IYVB8NfiRqhdZlTxjspNh",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b27355de63b8aaf464fe8146b4f1",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e0255de63b8aaf464fe8146b4f1",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d0000485155de63b8aaf464fe8146b4f1",
            "width": 64
          }
        ],
        "name": "Rainbow",
        "release_date": "2017-08-11",
        "release_date_precision": "day",
        "total_tracks": 14,
        "type": "album",
        "uri": "spotify:album:1IYVB8NfiRqhdZlTxjspNh"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/6LqNN22kT3074XbTVUrhzX"
          },
          "href": "https://api.spotify.com/v1/artists/6LqNN22kT3074XbTVUrhzX",
          "id": "6LqNN22kT3074XbTVUrhzX",
          "name": "Kesha",
          "type": "artist",
          "uri": "spotify:artist:6LqNN22kT3074XbTVUrhzX"
        },
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/02uYdhMhCgdB49hZlYRm9o"
          },
          "href": "https://api.spotify.com/v1/artists/02uYdhMhCgdB49hZlYRm9o",
          "id": "02uYdhMhCgdB49hZlYRm9o",
          "name": "Eagles Of Death Metal",
          "type": "artist",
          "uri": "spotify:artist:02uYdhMhCgdB49hZlYRm9o"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 185813,
      "explicit": true,
      "external_ids": {
        "isrc": "USRC11701505"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/1nxufatvWIGPPBtPACXzu8"
      },
      "href": "https://api.spotify.com/v1/tracks/1nxufatvWIGPPBtPACXzu8",
      "id": "1nxufatvWIGPPBtPACXzu8",
      "is_local": false,
      "name": "Let 'Em Talk (feat. Eagles of Death Metal)",
      "popularity": 48,
      "preview_url": "https://p.scdn.co/mp3-preview/25539e95f3b1331af0d97d4a103cf95ad0f0cf65?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 2,
      "type": "track",
      "uri": "spotify:track:1nxufatvWIGPPBtPACXzu8"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3QLIkT4rD2FMusaqmkepbq"
            },
            "href": "https://api.spotify.com/v1/artists/3QLIkT4rD2FMusaqmkepbq",
            "id": "3QLIkT4rD2FMusaqmkepbq",
            "name": "Rachel Platten",
            "type": "artist",
            "uri": "spotify:artist:3QLIkT4rD2FMusaqmkepbq"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/3lj5OMBx3uExb8Br7GR7Az"
        },
        "href": "https://api.spotify.com/v1/albums/3lj5OMBx3uExb8Br7GR7Az",
        "id": "3lj5OMBx3uExb8Br7GR7Az",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273f4dead4bcc5e681b9485bdf4",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02f4dead4bcc5e681b9485bdf4",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851f4dead4bcc5e681b9485bdf4",
            "width": 64
          }
        ],
        "name": "Wildfire (Japan Version)",
        "release_date": "2016-04-13",
        "release_date_precision": "day",
        "total_tracks": 17,
        "type": "album",
        "uri": "spotify:album:3lj5OMBx3uExb8Br7GR7Az"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/3QLIkT4rD2FMusaqmkepbq"
          },
          "href": "https://api.spotify.com/v1/artists/3QLIkT4rD2FMusaqmkepbq",
          "id": "3QLIkT4rD2FMusaqmkepbq",
          "name": "Rachel Platten",
          "type": "artist",
          "uri": "spotify:artist:3QLIkT4rD2FMusaqmkepbq"
        },
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/1vWImodgVqIgTUkekGEfR9"
          },
          "href": "https://api.spotify.com/v1/artists/1vWImodgVqIgTUkekGEfR9",
          "id": "1vWImodgVqIgTUkekGEfR9",
          "name": "Dave Aud\u00e9",
          "type": "artist",
          "uri": "spotify:artist:1vWImodgVqIgTUkekGEfR9"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 201320,
      "explicit": false,
      "external_ids": {
        "isrc": "USSM11507954"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/42ykPynBdDNcuUSrp01Brj"
      },
      "href": "https://api.spotify.com/v1/tracks/42ykPynBdDNcuUSrp01Brj",
      "id": "42ykPynBdDNcuUSrp01Brj",
      "is_local": false,
      "name": "Fight Song - Dave Aude Remix",
      "popularity": 3,
      "preview_url": "https://p.scdn.co/mp3-preview/c1597ea57e17f5414f17d94a90d8931c3e8f2497?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 16,
      "type": "track",
      "uri": "spotify:track:42ykPynBdDNcuUSrp01Brj"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6ueGR6SWhUJfvEhqkvMsVs"
            },
            "href": "https://api.spotify.com/v1/artists/6ueGR6SWhUJfvEhqkvMsVs",
            "id": "6ueGR6SWhUJfvEhqkvMsVs",
            "name": "Janelle Mon\u00e1e",
            "type": "artist",
            "uri": "spotify:artist:6ueGR6SWhUJfvEhqkvMsVs"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/7MvSB0JTdtl1pSwZcgvYQX"
        },
        "href": "https://api.spotify.com/v1/albums/7MvSB0JTdtl1pSwZcgvYQX",
        "id": "1rW6UUZRQWW34j4zCQDkfX",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273120a1366324c2ae1728e17e5",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02120a1366324c2ae1728e17e5",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851120a1366324c2ae1728e17e5",
            "width": 64
          }
        ],
        "name": "The ArchAndroid",
        "release_date": "2010-05-17",
        "release_date_precision": "day",
        "total_tracks": 18,
        "type": "album",
        "uri": "spotify:album:7MvSB0JTdtl1pSwZcgvYQX"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/6ueGR6SWhUJfvEhqkvMsVs"
          },
          "href": "https://api.spotify.com/v1/artists/6ueGR6SWhUJfvEhqkvMsVs",
          "id": "6ueGR6SWhUJfvEhqkvMsVs",
          "name": "Janelle Mon\u00e1e",
          "type": "artist",
          "uri": "spotify:artist:6ueGR6SWhUJfvEhqkvMsVs"
        },
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/2ht3wxeT69CzyKFChNnNAB"
          },
          "href": "https://api.spotify.com/v1/artists/2ht3wxeT69CzyKFChNnNAB",
          "id": "2ht3wxeT69CzyKFChNnNAB",
          "name": "Big Boi",
          "type": "artist",
          "uri": "spotify:artist:2ht3wxeT69CzyKFChNnNAB"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 262586,
      "explicit": false,
      "external_ids": {
        "isrc": "USBB41000024"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/1ljzHUgt2SU2ADkhfa9eBC"
      },
      "href": "https://api.spotify.com/v1/tracks/1ljzHUgt2SU2ADkhfa9eBC",
      "id": "1ljzHUgt2SU2ADkhfa9eBC",
      "is_local": false,
      "name": "Tightrope (feat. Big Boi) - Big Boi Vocal Edit",
      "popularity": 56,
      "preview_url": "https://p.scdn.co/mp3-preview/58cff379542f16b6d174d66c18fd7c0d49616486?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 7,
      "type": "track",
      "uri": "spotify:track:1ljzHUgt2SU2ADkhfa9eBC"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5wugb0kaq0J6nyQ5Xgd17i"
            },
            "href": "https://api.spotify.com/v1/artists/5wugb0kaq0J6nyQ5Xgd17i",
            "id": "5wugb0kaq0J6nyQ5Xgd17i",
            "name": "Aly & AJ",
            "type": "artist",
            "uri": "spotify:artist:5wugb0kaq0J6nyQ5Xgd17i"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/7A3E3rRsRIQgovrIp7S3aM"
        },
        "href": "https://api.spotify.com/v1/albums/7A3E3rRsRIQgovrIp7S3aM",
        "id": "7A3E3rRsRIQgovrIp7S3aM",
        "name": "Ten Years (Deluxe)",
        "release_date": "2018-11-30",
        "release_date_precision": "day",
        "total_tracks": 8,
        "type": "album",
        "uri": "spotify:album:7A3E3rRsRIQgovrIp7S3aM"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/5wugb0kaq0J6nyQ5Xgd17i"
          },
          "href": "https://api.spotify.com/v1/artists/5wugb0kaq0J6nyQ5Xgd17i",
          "id": "5wugb0kaq0J6nyQ5Xgd17i",
          "name": "Aly & AJ",
          "type": "artist",
          "uri": "spotify:artist:5wugb0kaq0J6nyQ5Xgd17i"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 211960,
      "explicit": false,
      "external_ids": {
        "isrc": "GBKPL1786315"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/41Vu4jOXWmpznLRWJnBX0Y"
      },
      "href": "https://api.spotify.com/v1/tracks/41Vu4jOXWmpznLRWJnBX0Y",
      "id": "41Vu4jOXWmpznLRWJnBX0Y",
      "is_local": false,
      "name": "Take Me",
      "popularity": 47,
      "preview_url": "https://p.scdn.co/mp3-preview/41252148f0eccd4dd02e9a2d9ecfa52b10bf1514?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:41Vu4jOXWmpznLRWJnBX0Y"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/50VoYemccTaftNfFqWtlXd"
            },
            "href": "https://api.spotify.com/v1/artists/50VoYemccTaftNfFqWtlXd",
            "id": "50VoYemccTaftNfFqWtlXd",
            "name": "Superfruit",
            "type": "artist",
            "uri": "spotify:artist:50VoYemccTaftNfFqWtlXd"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/1j6xIP5xwMw8MMp8x9gMuR"
        },
        "href": "https://api.spotify.com/v1/albums/1j6xIP5xwMw8MMp8x9gMuR",
        "id": "1j6xIP5xwMw8MMp8x9gMuR",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273ec505d3fa84ddd8f0d5b976a",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02ec505d3fa84ddd8f0d5b976a",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851ec505d3fa84ddd8f0d5b976a",
            "width": 64
          }
        ],
        "release_date": "2017-06-30",
        "release_date_precision": "day",
        "total_tracks": 7,
        "type": "album",
        "uri": "spotify:album:1j6xIP5xwMw8MMp8x9gMuR"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/50VoYemccTaftNfFqWtlXd"
          },
          "href": "https://api.spotify.com/v1/artists/50VoYemccTaftNfFqWtlXd",
          "id": "50VoYemccTaftNfFqWtlXd",
          "name": "Superfruit",
          "type": "artist",
          "uri": "spotify:artist:50VoYemccTaftNfFqWtlXd"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 194800,
      "explicit": false,
      "external_ids": {
        "isrc": "USRC11701388"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/2bopUyK6ll0CZFw03TDKAY"
      },
      "href": "https://api.spotify.com/v1/tracks/2bopUyK6ll0CZFw03TDKAY",
      "id": "6p6KdVpfKtTMisH5VfWqsL",
      "is_local": false,
      "name": "Imaginary Parties",
      "popularity": 39,
      "preview_url": "https://p.scdn.co/mp3-preview/1b6723578b62e6832f477c9115c88172924ea56c?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:2bopUyK6ll0CZFw03TDKAY"
    },
    {
      "album": {
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5ivCbtrcD5N4rD337xIb2z"
            },
            "href": "https://api.spotify.com/v1/artists/5ivCbtrcD5N4rD337xIb2z",
            "id": "5ivCbtrcD5N4rD337xIb2z",
            "name": "MisterWives",
            "type": "artist",
            "uri": "spotify:artist:5ivCbtrcD5N4rD337xIb2z"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/7IKJjUUm2V7xnOwEnIUga9"
        },
        "href": "https://api.spotify.com/v1/albums/7IKJjUUm2V7xnOwEnIUga9",
        "id": "7IKJjUUm2V7xnOwEnIUga9",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273e203097ca2660dc880294d6a",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02e203097ca2660dc880294d6a",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851e203097ca2660dc880294d6a",
            "width": 64
          }
        ],
        "name": "Never Give Up On Me",
        "release_date": "2017-10-27",
        "release_date_precision": "day",
        "total_tracks": 1,
        "type": "album",
        "uri": "spotify:album:7IKJjUUm2V7xnOwEnIUga9"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/5ivCbtrcD5N4rD337xIb2z"
          },
          "href": "https://api.spotify.com/v1/artists/5ivCbtrcD5N4rD337xIb2z",
          "id": "5ivCbtrcD5N4rD337xIb2z",
          "name": "MisterWives",
          "type": "artist",
          "uri": "spotify:artist:5ivCbtrcD5N4rD337xIb2z"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 174266,
      "explicit": false,
      "external_ids": {
        "isrc": "USUM71711841"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/7LuyQo3nlMV2cETpsDLWsQ"
      },
      "href": "https://api.spotify.com/v1/tracks/7LuyQo3nlMV2cETpsDLWsQ",
      "id": "7LuyQo3nlMV2cETpsDLWsQ",
      "is_local": false,
      "name": "Never Give Up On Me",
      "popularity": 42,
      "preview_url": null,
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:7LuyQo3nlMV2cETpsDLWsQ"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3BmGtnKgCSGYIUhmivXKWX"
            },
            "href": "https://api.spotify.com/v1/artists/3BmGtnKgCSGYIUhmivXKWX",
            "id": "3BmGtnKgCSGYIUhmivXKWX",
            "name": "Kelly Clarkson",
            "type": "artist",
            "uri": "spotify:artist:3BmGtnKgCSGYIUhmivXKWX"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/7oKtXc3FkeOZTCB88YugON"
        },
        "href": "https://api.spotify.com/v1/albums/7oKtXc3FkeOZTCB88YugON",
        "id": "7oKtXc3FkeOZTCB88YugON",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b2738612619562d9e86624479ec8",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e028612619562d9e86624479ec8",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d000048518612619562d9e86624479ec8",
            "width": 64
          }
        ],
        "name": "Piece By Piece (Deluxe Version)",
        "release_date": "2015-02-27",
        "release_date_precision": "day",
        "total_tracks": 16,
        "type": "album",
        "uri": "spotify:album:7oKtXc3FkeOZTCB88YugON"
      },
      "artists": [],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 198733,
      "explicit": false,
      "external_ids": {
        "isrc": "GBCTA1400065"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/7FC9Lng8iXU081lbigu8m8"
      },
      "href": "https://api.spotify.com/v1/tracks/7FC9Lng8iXU081lbigu8m8",
      "id": "7FC9Lng8iXU081lbigu8m8",
      "is_local": false,
      "name": "Heartbeat Song",
      "popularity": 67,
      "preview_url": "https://p.scdn.co/mp3-preview/bf083c904ad9f4ffa21031dad2e372594ec25e56?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:7FC9Lng8iXU081lbigu8m8"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3whuHq0yGx60atvA2RCVRW"
            },
            "href": "https://api.spotify.com/v1/artists/3whuHq0yGx60atvA2RCVRW",
            "id": "3whuHq0yGx60atvA2RCVRW",
            "name": "Olly Murs",
            "type": "artist",
            "uri": "spotify:artist:3whuHq0yGx60atvA2RCVRW"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/2OvZ8JCShhvxNkptwoGjve"
        },
        "href": "https://api.spotify.com/v1/albums/2OvZ8JCShhvxNkptwoGjve",
        "id": "2OvZ8JCShhvxNkptwoGjve",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273ff2057b7343d2233451ff8e7",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02ff2057b7343d2233451ff8e7",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851ff2057b7343d2233451ff8e7",
            "width": 64
          }
        ],
        "name": "In Case You Didn't Know",
        "release_date": "2011-11-28",
        "release_date_precision": "day",
        "total_tracks": 13,
        "type": "album",
        "uri": "spotify:album:2OvZ8JCShhvxNkptwoGjve"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/3whuHq0yGx60atvA2RCVRW"
          },
          "href": "https://api.spotify.com/v1/artists/3whuHq0yGx60atvA2RCVRW",
          "id": "3whuHq0yGx60atvA2RCVRW",
          "name": "Olly Murs",
          "type": "artist",
          "uri": "spotify:artist:3whuHq0yGx60atvA2RCVRW"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 202226,
      "explicit": false,
      "external_ids": {
        "isrc": "GBARL1101197"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/1FSWSs9CL01RCYxXtm08Rf"
      },
      "href": "https://api.spotify.com/v1/tracks/1FSWSs9CL01RCYxXtm08Rf",
      "id": "1FSWSs9CL01RCYxXtm08Rf",
      "is_local": false,
      "name": "Dance with Me Tonight",
      "popularity": 70,
      "preview_url": "https://p.scdn.co/mp3-preview/882a4b1505b9bedf8fe156080cebb23193b3540b?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 3,
      "type": "track",
      "uri": "spotify:track:1FSWSs9CL01RCYxXtm08Rf"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3QLIkT4rD2FMusaqmkepbq"
            },
            "href": "https://api.spotify.com/v1/artists/3QLIkT4rD2FMusaqmkepbq",
            "id": "3QLIkT4rD2FMusaqmkepbq",
            "name": "Rachel Platten",
            "type": "artist",
            "uri": "spotify:artist:3QLIkT4rD2FMusaqmkepbq"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/1mH4ntQRUk1akxx6WNST8q"
        },
        "href": "https://api.spotify.com/v1/albums/1mH4ntQRUk1akxx6WNST8q",
        "id": "1mH4ntQRUk1akxx6WNST8q",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b27379a74bed80ea8e2ac850af1f",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e0279a74bed80ea8e2ac850af1f",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d0000485179a74bed80ea8e2ac850af1f",
            "width": 64
          }
        ],
        "name": "Waves",
        "release_date": "2017-10-27",
        "release_date_precision": "day",
        "total_tracks": 13,
        "type": "album",
        "uri": "spotify:album:1mH4ntQRUk1akxx6WNST8q"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/3QLIkT4rD2FMusaqmkepbq"
          },
          "href": "https://api.spotify.com/v1/artists/3QLIkT4rD2FMusaqmkepbq",
          "id": "3QLIkT4rD2FMusaqmkepbq",
          "name": "Nitish Gupta",
          "type": "artist",
          "uri": "spotify:artist:3QLIkT4rD2FMusaqmkepbq"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 175333,
      "explicit": false,
      "external_ids": {
        "isrc": "USSM11708390"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/5yjOhc3JKrznGouRHMagoJ"
      },
      "href": "https://api.spotify.com/v1/tracks/5yjOhc3JKrznGouRHMagoJ",
      "id": "5yjOhc3JKrznGouRHMagoJ",
      "is_local": false,
      "name": "Redundant Track Name",
      "popularity": 50,
      "preview_url": "https://p.scdn.co/mp3-preview/418a06d953fcf4dff106dcf727b06d9018e37b47?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 6,
      "type": "track",
      "uri": "spotify:track:5yjOhc3JKrznGouRHMagoJ"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0X2BH1fck6amBIoJhDVmmJ"
            },
            "href": "https://api.spotify.com/v1/artists/0X2BH1fck6amBIoJhDVmmJ",
            "id": "0X2BH1fck6amBIoJhDVmmJ",
            "name": "Ellie Goulding",
            "type": "artist",
            "uri": "spotify:artist:0X2BH1fck6amBIoJhDVmmJ"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/44va7sFuK8IGzrj0BIX8kK"
        },
        "href": "https://api.spotify.com/v1/albums/44va7sFuK8IGzrj0BIX8kK",
        "id": "44va7sFuK8IGzrj0BIX8kK",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273156d79bdb60fc5f7af75590b",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02156d79bdb60fc5f7af75590b",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851156d79bdb60fc5f7af75590b",
            "width": 64
          }
        ],
        "name": "Brightest Blue",
        "release_date": "2020-07-16",
        "release_date_precision": "day",
        "total_tracks": 19,
        "type": "album",
        "uri": "spotify:album:44va7sFuK8IGzrj0BIX8kK"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/0X2BH1fck6amBIoJhDVmmJ"
          },
          "href": "https://api.spotify.com/v1/artists/0X2BH1fck6amBIoJhDVmmJ",
          "id": "0X2BH1fck6amBIoJhDVmmJ",
          "name": "Ellie Goulding",
          "type": "artist",
          "uri": "spotify:artist:0X2BH1fck6amBIoJhDVmmJ"
        }
      ],
      "available_markets": [],
      "disc_number": 2,
      "duration_ms": 201226,
      "explicit": false,
      "external_ids": {
        "isrc": "GBUM71901344"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/6p6KdVpfKtTMisH5VfWqsL"
      },
      "href": "https://api.spotify.com/v1/tracks/6p6KdVpfKtTMisH5VfWqsL",
      "id": "6p6KdVpfKtTMisH5VfWqsL",
      "is_local": false,
      "name": "Redundant Track Name",
      "popularity": 61,
      "preview_url": null,
      "track_number": 6,
      "type": "track",
      "uri": "spotify:track:6p6KdVpfKtTMisH5VfWqsL"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4VhL8KLjVso4vLfOLVViTb"
            },
            "href": "https://api.spotify.com/v1/artists/4VhL8KLjVso4vLfOLVViTb",
            "id": "4VhL8KLjVso4vLfOLVViTb",
            "name": "Nitish Gupta",
            "type": "artist",
            "uri": "spotify:artist:4VhL8KLjVso4vLfOLVViTb"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/114sumrk5wTeMWHVin86QC"
        },
        "href": "https://api.spotify.com/v1/albums/114sumrk5wTeMWHVin86QC",
        "id": "114sumrk5wTeMWHVin86QC",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273c0758d813c09f649f630f405",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02c0758d813c09f649f630f405",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851c0758d813c09f649f630f405",
            "width": 64
          }
        ],
        "name": "Hello My Name Is...",
        "release_date": "2012-01-01",
        "release_date_precision": "day",
        "total_tracks": 12,
        "type": "album",
        "uri": "spotify:album:114sumrk5wTeMWHVin86QC"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/4VhL8KLjVso4vLfOLVViTb"
          },
          "href": "https://api.spotify.com/v1/artists/4VhL8KLjVso4vLfOLVViTb",
          "id": "4VhL8KLjVso4vLfOLVViTb",
          "name": "Nitish Gupta",
          "type": "artist",
          "uri": "spotify:artist:4VhL8KLjVso4vLfOLVViTb"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 200946,
      "explicit": false,
      "external_ids": {
        "isrc": "USHR11233750"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/5xvUgoVED1F4mBu8FL0HaW"
      },
      "href": "https://api.spotify.com/v1/tracks/5xvUgoVED1F4mBu8FL0HaW",
      "id": "5xvUgoVED1F4mBu8FL0HaW",
      "is_local": false,
      "name": "Ready or Not",
      "popularity": 73,
      "preview_url": null,
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:5xvUgoVED1F4mBu8FL0HaW"
    },
    {
      "album": {
        "album_type": "ALBUM",
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1l8Fu6IkuTP0U5QetQJ5Xt"
            },
            "href": "https://api.spotify.com/v1/artists/1l8Fu6IkuTP0U5QetQJ5Xt",
            "id": "1l8Fu6IkuTP0U5QetQJ5Xt",
            "name": "Fifth Harmony",
            "type": "artist",
            "uri": "spotify:artist:1l8Fu6IkuTP0U5QetQJ5Xt"
          }
        ],
        "available_markets": [],
        "external_urls": {
          "spotify": "https://open.spotify.com/album/0pF0oyuPNdOObniB1Ng0kW"
        },
        "href": "https://api.spotify.com/v1/albums/0pF0oyuPNdOObniB1Ng0kW",
        "id": "0pF0oyuPNdOObniB1Ng0kW",
        "images": [
          {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b273d03fa6f4e758282b7920b5c8",
            "width": 640
          },
          {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e02d03fa6f4e758282b7920b5c8",
            "width": 300
          },
          {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d00004851d03fa6f4e758282b7920b5c8",
            "width": 64
          }
        ],
        "name": "7/27 (Deluxe)",
        "release_date": "2016-05-27",
        "release_date_precision": "day",
        "total_tracks": 12,
        "type": "album",
        "uri": "spotify:album:0pF0oyuPNdOObniB1Ng0kW"
      },
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/1l8Fu6IkuTP0U5QetQJ5Xt"
          },
          "href": "https://api.spotify.com/v1/artists/1l8Fu6IkuTP0U5QetQJ5Xt",
          "id": "1l8Fu6IkuTP0U5QetQJ5Xt",
          "name": "Fifth Harmony",
          "type": "artist",
          "uri": "spotify:artist:1l8Fu6IkuTP0U5QetQJ5Xt"
        },
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/7c0XG5cIJTrrAgEC3ULPiq"
          },
          "href": "https://api.spotify.com/v1/artists/7c0XG5cIJTrrAgEC3ULPiq",
          "id": "7c0XG5cIJTrrAgEC3ULPiq",
          "name": "Ty Dolla $ign",
          "type": "artist",
          "uri": "spotify:artist:7c0XG5cIJTrrAgEC3ULPiq"
        }
      ],
      "available_markets": [],
      "disc_number": 1,
      "duration_ms": 214480,
      "explicit": false,
      "external_ids": {
        "isrc": "USSM11600251"
      },
      "external_urls": {
        "spotify": "https://open.spotify.com/track/4tCtwWceOPWzenK2HAIJSb"
      },
      "href": "https://api.spotify.com/v1/tracks/4tCtwWceOPWzenK2HAIJSb",
      "is_local": false,
      "name": "Work from Home (feat. Ty Dolla $ign)",
      "popularity": 78,
      "preview_url": "https://p.scdn.co/mp3-preview/b2d6e6ea9163eb361f5406f75264de490243964a?cid=bd6a887dce7247ecb570fda88090afd8",
      "track_number": 2,
      "type": "track",
      "uri": "spotify:track:4tCtwWceOPWzenK2HAIJSb"
    }
  ],
  "seeds": [
    {
      "initialPoolSize": 249,
      "afterFilteringSize": 249,
      "afterRelinkingSize": 249,
      "id": "11dFghVXANMlKmJXsNCbNl",
      "type": "TRACK",
      "href": "https://api.spotify.com/v1/tracks/11dFghVXANMlKmJXsNCbNl"
    }
  ]
}
'''