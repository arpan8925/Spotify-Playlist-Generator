import requests
import base64
from bs4 import BeautifulSoup

SONG_END = "https://www.jiosaavn.com/featured/trending_today/I3kvhipIy73uCJW60TJk1Q__"

ACCESS_END = "https://accounts.spotify.com/api/token"



def spotify_access_token():

    CLIENT_ID_encode = base64.b64encode(b'ccfc3e0244884379a0b514be1737b83d')

    access_head = {
        "Authorization" : f"Basic {CLIENT_ID_encode}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    access_body = {
        "grant_type": 'client_credentials'
    }



    return spotify_access_token
w
def get_song_details():
    song_response = requests.get(SONG_END)
    if song_response.status_code == 200:
        soup = BeautifulSoup(song_response.content, "html.parser")
        song_titles = [title.getText() for title in soup.find_all(name="a", class_="u-color-js-gray")]
        print(song_titles)
    else:
        print(f"Failed to retrieve the page. Status code: {song_response.status_code}")


get_song_details()
