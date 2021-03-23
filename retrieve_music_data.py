import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time


client_credentials_manager = SpotifyClientCredentials('CLIENT_ID', 'CLIENT_SECRET')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
ids = []

def getPlaylistTrackIDs(user, playlist_id):
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])

    return ids

playlist_ids = ['37i9dQZF1DWWzQTBs5BHX9', '37i9dQZF1DX1vSJnMeoy3V', '37i9dQZF1DX3j9EYdzv2N9', '37i9dQZF1DWYuGZUE4XQXm','37i9dQZF1DX4UkKv8ED8jp']

for i in playlist_ids:
    print(i)
    ids = getPlaylistTrackIDs('Spotify', i)


def getTrackFeatures(id):
    general = sp.track(id)
    features = sp.audio_features(id)

    #general
    name = general['name']
    album = general['album']['name']
    artist = general['album']['artists'][0]['name']
    release_date = general['album']['release_date']
    length = general['duration_ms']
    popularity = general['popularity']

    # Features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']

    track = [name, album, artist, release_date, length, popularity, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
    return track


tracks = []
for i in range(0, 500):
    if (i % 50 == 0 &  i != 0) :
        time.sleep(180)
    time.sleep(.5)
    track = getTrackFeatures(ids[i])
    tracks.append(track)
    print(i)

df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
df.to_csv("/Users/emilywang/Development/artist-music-analyzer/top_hits_by_year_late_thousands.csv", sep = ',')
