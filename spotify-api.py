# https://spotipy.readthedocs.io/en/latest/#non-authorized-requests
# https://github.com/plamere/spotipy/issues/194
# https://stackoverflow.com/questions/32956443/invalid-redirect-uri-on-spotify-auth

import spotipy
import spotipy.util as util

username = 'USERNAME-HERE'
scope = 'user-library-read'
client_id = 'CLIENT-ID-HERE'
client_secret = 'CLIENT-SECRET-HERE'
redirect_uri = 'https://example.com/callback'

# User authentication via web browser
token = util.prompt_for_user_token(
        username = username, scope = scope,
        client_id = client_id, client_secret = client_secret,
        redirect_uri = redirect_uri)

# create authorized instance
spotify = spotipy.Spotify(auth=token)

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        #print("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))
        row = [playlist['name'], track['artists'][0]['name'],  track['name']]
        rows.append(row)
        
username = 'USERNAME-HERE'
rows = []
sp = spotipy.Spotify(auth=token)
playlists = sp.user_playlists(username)
for playlist in playlists['items']:
    if playlist['owner']['id'] == username:
        results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
        tracks = results['tracks']
        show_tracks(tracks)
        while tracks['next']:
            tracks = sp.next(tracks)
            show_tracks(tracks)
            
# export as .csv
df = pd.DataFrame(rows)
df.to_csv('spotify-playlist-tracks.csv')
