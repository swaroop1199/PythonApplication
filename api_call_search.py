import requests
from requests import get
import base64
import json

def gettoken():
    # Spotify API credentials
    client_id = "b0be9b6d28044908b21c9e7e6c5e5c85"
    client_secret = "6cfe6965f50f4210895b0cb463d3991c"


    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")


    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}"
    }
    data = {
        "grant_type": "client_credentials"
    }

    # Send POST request to get the token
    response = requests.post(url, headers=headers, data=data)
    json_result = json.loads(response.content)
    token = json_result["access_token"]
    return token


def auth(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artistname):
    url = "https://api.spotify.com/v1/search"
    headers = auth(token)
    query = f"?q={artistname}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url,headers=headers)
    json_result = json.loads(result.content)
    print(json_result)

token=gettoken()
search_for_artist(token,"arijit singh")

















#Base_URL = 'https://api.spotify.com/v1/users/31mlbxzeo7s2lqyobqvgucwwj6qe/playlists'
#ACCESS_TOKEN = 'BQD-5yZgBm-7lnIZvTU2Z2HBPbWuyBm5-W05R4pLYH-JB6KL7wyVSF7lfEHBFc8Aj-h8ZHAyjRn99_UCQ3-EA7KFLndo5TNPdhjLP45xzzD1GqeLUsQ'


#def create_playlist_on_spotify(name, public):
##    response = requests.post(Base_URL,headers={"Authorization": f"Bearer {ACCESS_TOKEN}"},
 #                            json={
 #                                "name":name,
 #                                "public":public
 #                            })
 #   json_resp = response.json()
 #   return json_resp
