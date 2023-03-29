
import random
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import json


with open("credentials.json") as file:
    data = json.load(file)


SCOPE = "user-library-read"
REDIRECT_URI = "http://localhost:8888/callback"
USERNAME = data["SPOTIFY_USERNAME"]
CLIENT_ID = data["SPOTIFY_CLIENT_ID"]
CLIENT_SECRET = data["SPOTIFY_CLIENT_SECRET"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, redirect_uri=REDIRECT_URI, 
                                                username=USERNAME, client_id=CLIENT_ID, 
                                                client_secret=CLIENT_SECRET))

def suggest_song(mood):
    # Get recommended tracks based on mood
    recommendations = sp.recommendations(seed_genres=[mood], limit=20)
    tracks = recommendations["tracks"]
    
    if not tracks:
        return "Sorry, I couldn't find any songs that match your mood."
    
    # Choose a random track from the results
    track = random.choice(tracks)
    artist = track["artists"][0]["name"]
    song_name = track["name"]
    preview_url = track["preview_url"]
    
    message = f"How about '{song_name}' by {artist}?"
    return message
'''
# Example usage:
while True:
    mood = input("How are you feeling today? ")
    suggestion = suggest_song(mood)
    print(suggestion)'''