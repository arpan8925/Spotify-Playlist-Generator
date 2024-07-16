import requests
import base64
import base64
from bs4 import BeautifulSoup
from spotipy import *

SONG_END = "https://www.jiosaavn.com/featured/trending_today/I3kvhipIy73uCJW60TJk1Q__"
Spotify_Id = "f409f6r9hrprb8brt7l0djqvi"
ACCESS_END = "https://accounts.spotify.com/api/token"
SPOTIFY_END = "https://api.spotify.com/v1"

sp = Spotify(auth_manager=SpotifyOAuth(client_id="ccfc3e0244884379a0b514be1737b83d",
                                               client_secret="b57f44b97b1f43aab4a22b6128404eca",
                                               redirect_uri="http://localhost:3000",
                                               scope="user-library-read"))

playlist = user_playlist_create(Spotify_Id, name='New Playlist', public=True, collaborative=False, description='New Playlist Desc')



# def create_playlist(access_token):
#     playsit_crt_end = f"{SPOTIFY_END}/users/{Spotify_Id}/playlists"

#     playlist_head = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/json"
#     }

#     playlist_body = {
#         "name": "New Playlist",
#         "description": "New playlist description",
#         "public": True
#     }

#     response = requests.post(playsit_crt_end, headers=playlist_head, json=playlist_body)

#     if response.status_code == 201:
#         playlist_info = response.json()
#         print(f"Playlist created: {playlist_info}")
#         return playlist_info
#     else:
#         print(f"Failed to create playlist. Status code: {response.status_code}")
#         print(response.json())
#         return None

    

# def get_song_details():
#     song_response = requests.get(SONG_END)
#     if song_response.status_code == 200:
#         soup = BeautifulSoup(song_response.content, "html.parser")
#         song_titles = [title.getText() for title in soup.find_all(name="a", class_="u-color-js-gray")]
#         print(song_titles)
#     else:
#         print(f"Failed to retrieve the page. Status code: {song_response.status_code}")


# get_song_details()

