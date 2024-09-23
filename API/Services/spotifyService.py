import base64
from config import load_config
import requests

def get_access_token():
    global token, config_dict
    config_dict = load_config("database.ini", "spotify")

    client_id = config_dict["client_id"]
    client_secret = config_dict["client_secret"]

    auth_string=f"{client_id}:{client_secret}"
    encoded_auth = base64.b64encode(auth_string.encode()).decode("utf-8")

    auth_header = f"Basic {encoded_auth}"

    url = "https://accounts.spotify.com/api/token"
    headers={ "Authorization":auth_header}
    data = {
        "grant_type":"client_credentials"
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        token = 'Bearer ' + response.json().get("access_token")


def check_token_expired(func):
    response = requests.post('https://api.spotify.com/v1/search?q=adele&type=track&limit=1')

    if response.status_code == 401:
        get_access_token()

    return func

@check_token_expired
def get_song_from_title(title):
    endpoint = "https://api.spotify.com/v1/search"

    search_request = f"q={title}&type=track&market=FR&limit=5&offset=0"

    headers = {"Authorization":token}

    response = requests.get(endpoint+"?"+search_request, headers=headers)
    if response.status_code == 200:
        data = response.json().get("tracks").get("items")
        return data

@check_token_expired
def get_song_by_id(id):
    endpoint = "https://api.spotify.com/v1/tracks"

    headers = {"Authorization":token}

    response = requests.get(endpoint+f"/{id}", headers=headers)
    if response.status_code == 200:
        data = response.json()

        artists = data["artists"]
        idSong = data["id"]
        nameSong = data["name"]
        imgAlbum = data["album"]["images"]
        return data
    

if __name__ == "__main__":
    get_song_by_id("11mwFrKvLXCbcVGNxffGyP")