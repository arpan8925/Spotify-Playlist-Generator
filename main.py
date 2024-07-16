import requests
import base64
from bs4 import BeautifulSoup

SONG_END = "https://www.jiosaavn.com/featured/trending_today/I3kvhipIy73uCJW60TJk1Q__"

ACCESS_END = "https://accounts.spotify.com/api/token"

def spotify_access_token():
    # Define your client ID and client secret
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'

    # Encode client ID and client secret in base64
    client_credentials = f"{client_id}:{client_secret}"
    client_credentials_base64 = base64.b64encode(client_credentials.encode()).decode()

    # Set the headers and body for the POST request
    headers = {
        "Authorization": f"Basic {client_credentials_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    body = {
        "grant_type": "client_credentials"
    }

    # Make the POST request to get the access token
    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=body)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response to get the access token
        token_info = response.json()
        access_token = token_info.get('access_token')
        print(f"Access token: {access_token}")
        return access_token
    else:
        print(f"Failed to get access token. Status code: {response.status_code}")
        print(response.json())
        return None

def get_song_details():
    song_response = requests.get(SONG_END)
    if song_response.status_code == 200:
        soup = BeautifulSoup(song_response.content, "html.parser")
        song_titles = [title.getText() for title in soup.find_all(name="a", class_="u-color-js-gray")]
        print(song_titles)
    else:
        print(f"Failed to retrieve the page. Status code: {song_response.status_code}")


get_song_details()

spotify_access_token()
