import requests
from bs4 import BeautifulSoup

song_end = "https://www.jiosaavn.com/featured/trending_today/I3kvhipIy73uCJW60TJk1Q__"


def get_song_details():
    song_response = requests.get(song_end)
    if song_response.status_code == 200:
        soup = BeautifulSoup(song_response.content, "html.parser")
        song_titles = [title.getText() for title in soup.find_all(name="a", class_="u-color-js-gray")]
        print(song_titles)
    else:
        print(f"Failed to retrieve the page. Status code: {song_response.status_code}")


get_song_details()
