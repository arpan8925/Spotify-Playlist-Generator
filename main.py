import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth 

SPOTIFY_CLIENT_ID = "ccfc3e0244884379a0b514be1737b83d"
SPOTIFY_CLIENT_SECRET = "b57f44b97b1f43aab4a22b6128404eca"
SPOTIFY_REDIRECT_URI = "http://localhost:3000"
SONG_END = "https://www.jiosaavn.com/featured/trending_today/I3kvhipIy73uCJW60TJk1Q__"  

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="playlist-modify-public"
))

song_response = requests.get(SONG_END)
if song_response.status_code == 200:
    soup = BeautifulSoup(song_response.content, "html.parser")
    song_titles = [title.getText() for title in soup.find_all(name="a", class_="u-color-js-gray")]

    for song_name in song_titles[:2]:
        song_name = song_name
        search_music = sp.search(
            q=song_name,
            limit=1,
            offset=0,
            type='track',
            market=None
            )

        items = search_music["tracks"]["items"][0]["uri"]

        playlist_id = "5xmEzU0RuIOWsTyedGKTQf"  # Replace with the correct playlist ID

        try:
            # Add the track to the playlist
            add_item = sp.playlist_add_items(playlist_id, [items])
            print(add_item)
        except Exception as e:
            print(f"An error occurred: {e}")

else:
    print(f"Failed to retrieve the page. Status code: {song_response.status_code}")