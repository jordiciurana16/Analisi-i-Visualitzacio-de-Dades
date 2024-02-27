import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd

api_client_id = "2d24e72bccfc459d8c6eb1408f954097"
api_client_secret = "29126da8bfd742a39389cb3a03766b64"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id,api_client_secret))

artist_id = "7ltDVBr6mKbRvohxheJ9h1"

llista_artistes = []
def get_related(id):
    resposta = spotify.artist_related_artists(id)
    return resposta

result = get_related(artist_id)

llista_de_relacionats = []

for artist in result["artists"]:
    artista = {}
    artista["id"] = artist["id"]
    artista["origen"] = "Rosalia"
    artista["desti"] = artist["name"]
    artista["generes"] = artist["genres"]

    llista_de_relacionats.append(artista)

    result_2 = get_related(artista["id"])
    #print(result_2["artists"])

    for related_artist in result_2["artists"]:
        artista_relacionat = {}
        artista_relacionat["id"] = related_artist["id"]
        artista_relacionat["origen"] = artista["desti"]
        artista_relacionat["desti"] = related_artist["name"]
        artista_relacionat["generes"] = related_artist["genres"]

        llista_de_relacionats.append(artista_relacionat)

llista_de_tuples = []

for i in llista_de_relacionats:
    source = i["origen"]
    target = i["desti"]
    tupla = (source, target)
    llista_de_tuples.append(tupla)

    for i in llista_de_relacionats:
        for g in i["generes"]:
            source = i["origen"]
            target = g
            tupla = (source, target)
            llista_de_tuples.append(tupla)


#print(llista_de_relacionats)
#print(llista_de_tuples)

df = pd.DataFrame(llista_de_tuples, columns = ["source", "target"])

print(df)

df.to_csv("graf.csv", sep=",",index=False)