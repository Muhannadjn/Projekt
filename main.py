import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from fastapi import FastAPI, File, UploadFile
import librosa
import tkinter as tk
import webbrowser

# Spotify API credentials setup
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id='6010233a66504798a679459effe9fc88',
    client_secret='b58d958ad39e4c7fb5cf3634da35ce84'
))

# Initialize FastAPI app
app = FastAPI()

# Setup Tkinter window for color change
window = tk.Tk()
window.title('Humör Detektion')
window.geometry('360x800')
window.configure(bg='#5696b8')

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI is working!"}

# Function to change background color based on mood
def change_color_based_on_mood(mood: str):
    if mood == "calm":
        window.configure(bg='blue')
    elif mood == "energetic":
        window.configure(bg='red')
    elif mood == "happy":
        window.configure(bg='green')
    else:
        window.configure(bg='#5696b8')  # Standardfärg

# Function to get Spotify playlist based on mood
def get_playlist_for_mood(mood: str):
    playlists = {
        "calm": "spotify:playlist:YOUR_CALM_PLAYLIST_URI",
        "energetic": "spotify:playlist:YOUR_ENERGETIC_PLAYLIST_URI",
        "happy": "spotify:playlist:YOUR_HAPPY_PLAYLIST_URI",
    }
    return playlists.get(mood, "spotify:playlist:YOUR_DEFAULT_PLAYLIST_URI")

# Endpoint to upload and analyze a voice file
@app.post("/analyze-voice/")
async def analyze_voice(file: UploadFile = File(...)):
    audio_data, sr = librosa.load(file.file, sr=None)
    mood = "happy"  # Placeholder for mood detection (you can replace with real logic)
    
    # Change color based on detected mood
    change_color_based_on_mood(mood)
    
    # Get Spotify playlist based on mood
    playlist = get_playlist_for_mood(mood)
    
    return {
        "mood": mood,
        "playlist": playlist,
        "message": "Voice analyzed successfully!"
    }

# Function to open Spotify login link
def open_spotify_login():
    webbrowser.open("https://accounts.spotify.com/en/login")

# Run the Tkinter event loop in a separate thread or integrate with FastAPI
window.mainloop()
