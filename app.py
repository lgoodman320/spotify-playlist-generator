import spotipy
from dotenv import dotenv_values
import pprint

# [
#     {"song": "I Will Always Love You", "artist": "Whitney Houston"},
#     {"song": "Someone Like You", "artist": "Adele"},
#     {"song": "Say Something", "artist": "A Great Big World"},
#     {"song": "The Sound of Silence", "artist": "Simon & Garfunkel"},
#     {"song": "Hurt", "artist": "Johnny Cash"},
#     {"song": "Mad World", "artist": "Gary Jules"},
# ]

# Load .env file
config = dotenv_values(".env")

spot = spotipy.Spotify(
    auth_manager = spotipy.SpotifyOAuth(
        client_id = config["SPOTIFY_CLIENT_ID"],
        client_secret = config["SPOTIFY_CLIENT_SECRET"],
        redirect_uri="http://localhost:9999",
        scope="playlist-modify-private"
    )
)

current_user = spot.current_user()

assert current_user is not None

search_results = spot.search(q="Uptown Funk", type="track", limit=10)
tracks = [search_results["tracks"]["items"][0]["id"]]

# Create playlist
created_playlist = spot.user_playlist_create(
    current_user["id"],
    public=False,
    name="TESTING PLAYLIST FUN"
)

# Add songs to playlist
spot.user_playlist_add_tracks(current_user["id"], created_playlist["id"], tracks)