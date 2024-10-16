import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from fastapi import FastAPI, File, UploadFile
import librosa
import webbrowser

# Spotify API credentials setup
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id='6010233a66504798a679459effe9fc88',
    client_secret='b58d958ad39e4c7fb5cf3634da35ce84'
))

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI is working!"}

def get_playlist_for_mood(mood: str):
    playlists = {
        "calm": "spotify:playlist:YOUR_CALM_PLAYLIST_URI",
        "energetic": "spotify:playlist:YOUR_ENERGETIC_PLAYLIST_URI",
        "happy": "spotify:playlist:YOUR_HAPPY_PLAYLIST_URI",
    }
    return playlists.get(mood, "spotify:playlist:YOUR_DEFAULT_PLAYLIST_URI")

@app.post("/analyze-voice/")
async def analyze_voice(file: UploadFile = File(...)):
    audio_data, sr = librosa.load(file.file, sr=None)
    mood = "calm"  # Placeholder for mood detection
    playlist = get_playlist_for_mood(mood)
    return {
        "mood": mood,
        "playlist": playlist,
        "message": "Voice analyzed successfully!"
    }

def open_spotify_login():
    webbrowser.open("https://accounts.spotify.com/en/login")
