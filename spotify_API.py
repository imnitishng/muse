import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = '1e924efdc9874d968670d8d8ecd842d3'
CLIENT_SECRET = '5ee8b82db6f44d5dac13ffcd31c0cd5f'

sp = spotipy.Spotify(
    auth_manager = SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET))

print('Search Track: ')
query = input()
print('\n')

results = sp.search(q=query, limit=20)

for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])

# Track analysis
track1 = results['tracks']['items'][0]
id = track1['id']

# results = sp.audio_analysis(id)

# acousticness danceability
results = sp.audio_features(id)
print(results)
