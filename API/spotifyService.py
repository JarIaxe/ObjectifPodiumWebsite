import base64
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
        token = response.json().get("access_token")

if __name__ == "__main__":
    config = load_config("database.ini", "spotify")
    get_access_token(config)

    print(token)