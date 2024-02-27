import spotipy
import json
import pandas as pd

from spotipy.oauth2 import SpotifyClientCredentials

api_client_id = "c9ab65d618e34af8bb30b1cfad537105"
api_client_secret = "99f8f6a5e8de45cc996508fd3f7ea97c"

artist_id = "3Zyph9kkkEfTKaMQrLotUV"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id,api_client_secret))

response = spotify.artist_related_artists(artist_id)

artists = response["artists"]

artist_list = []

i = 0

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(response, f, indent=4)

for a in artists:
    i += 1
    name = a["name"]
    followers = a["followers"]["total"]
    link = a["external_urls"]["spotify"]
    id = a["id"]
    frame = pd.DataFrame ({
        "name": name,
        "id": id,
        "followers": followers,
        "link": link
    }, index=[i])

    artist_list.append(frame)
    final = pd.concat(artist_list)
    print(final)

    final.to_excel("dataset.xlsx")
    print("Done")


    ###