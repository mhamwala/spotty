import os
import spotipy
import requests
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"
user_id = 1139419156
playlist_id = "37i9dQZF1E8BKPvDxDZEtP"

load_dotenv() # take environment variables from .env.

auth_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
sp = spotipy.Spotify(auth_manager=auth_manager)

url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
playlistID = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
trackName = f""
print(url)
# url = "	https://api.spotify.com/v1/me"

payload={}
headers = {
  'Authorization': 'Bearer <>'
}

response = requests.request("GET", playlistID, headers=headers, data=payload)

print(response.text)