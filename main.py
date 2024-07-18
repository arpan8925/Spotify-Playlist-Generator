import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set your Spotify API credentials
SPOTIFY_CLIENT_ID = "ccfc3e0244884379a0b514be1737b83d"
SPOTIFY_CLIENT_SECRET = "b57f44b97b1f43aab4a22b6128404eca"
SPOTIFY_REDIRECT_URI = "http://localhost:3000"

# Initialize the Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="playlist-modify-public"
))

# Fetch and print your playlists to confirm the correct playlist ID
playlists = sp.current_user_playlists()
print("Your playlists:")
for playlist in playlists['items']:
    print(f"{playlist['name']} - {playlist['id']}")

playlist_id = "5xmEzU0RuIOWsTyedGKTQf"  # Replace with the correct playlist ID
items = ["spotify:track:59apoGrffgx8KqdsqXRlDk"]

try:
    # Add the track to the playlist
    add_item = sp.playlist_add_items(playlist_id, items)
    print(add_item)
except Exception as e:
    print(f"An error occurred: {e}")

# SONG_END = "https://www.jiosaavn.com/featured/trending_today/I3kvhipIy73uCJW60TJk1Q__"  

# playlist_name = "New Playlist"
# playlist_description = "New Playlist Desc"
# playlist = sp.user_playlist_create(
#     user=SPOTIFY_USER_ID,
#     name=playlist_name,
#     public=True,
#     description=playlist_description
# )

# song_name = "Agun lagaiya dilo kone"
# search_music = sp.search(
#     q=song_name,
#     limit=10,
#     offset=0,
#     type='track',
#     market=None
#     )

# print(search_music["tracks"]["items"][0])


# def get_song_details():
#     song_response = requests.get(SONG_END)
#     if song_response.status_code == 200:
#         soup = BeautifulSoup(song_response.content, "html.parser")
#         song_titles = [title.getText() for title in soup.find_all(name="a", class_="u-color-js-gray")]
#         print(song_titles)
#     else:
#         print(f"Failed to retrieve the page. Status code: {song_response.status_code}")


# get_song_details()
















# print(f"Playlist created: {playlist['name']} with ID {playlist['id']}")
