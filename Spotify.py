#Make you a list of the best musics in the year and month you choose if they exists in spotify
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT = "example"
SECRET = "example"
OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT,
        client_secret=SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user = sp.me()["id"]
date = input("The date number in YYYY-MM-DD format: ")
page = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}").text
soup = BeautifulSoup(page, "html.parser")
list = soup.find_all(name="h3", id="title-of-a-story")
final = []
for n in list:
    if "a-font-primary-bold-s" in n.get("class"):
        final.append(n.getText())
final = final[2:]
con = []
for element in final:
    con.append(element.strip())
songs = []
for n in con:
    result=sp.search(q=f"track: {n} year: {date.split('-')[0]}", type="track")
    try:
        n=result["tracks"]["items"][0]["uri"]
        songs.append(n)
    except:
        print(f"Song {n} was not found")
id=sp.user_playlist_create(user=user, name=f"HistoryList{date.split('-')[0]}-{date.split('-')[1]}-{date.split('-')[2]}",
                        public=False, description="For Project")

sp.user_playlist_add_tracks(user=user,playlist_id=id["id"],tracks=songs)
