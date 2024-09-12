import base64
import json
from config import load_config
import requests

def get_access_token(config):
    global token
    client_id = config["client_id"]
    client_secret = config["client_secret"]

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


def check_token_expired():
    response = requests.post('url')

    if response.status_code == 401:
        get_access_token(config)

def get_song(title):
    endpoint = "https://api.spotify.com/v1/search"

    search_request = f"q={title}&type=track&market=FR&limit=5&offset=0"

    headers = {"Authorization":token}

    response = requests.get(endpoint+"?"+search_request, headers=headers)
    if response.status_code == 200:
        data = response.json().get("tracks").get("items")
        print(data)


if __name__ == "__main__":
    global config
    config = load_config("database.ini", "spotify")
    get_access_token(config)
    get_song("Yellow")