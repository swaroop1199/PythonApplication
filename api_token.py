import requests
import base64



# Spotify API credentials
client_id = "b0be9b6d28044908b21c9e7e6c5e5c85"  # Replace with your Spotify Client ID
client_secret = "6cfe6965f50f4210895b0cb463d3991c"  # Replace with your Spotify Client Secret

# Encode client_id and client_secret in Base64
auth_string = f"{client_id}:{client_secret}"
auth_bytes = auth_string.encode("utf-8")
auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

# Authentication options
url = "https://accounts.spotify.com/api/token"
headers = {
    "Authorization": f"Basic {auth_base64}"
}
data = {
    "grant_type": "client_credentials"
}

# Send POST request to get the token
response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    token = response.json().get("access_token")
    print(f"Access token: {token}")
else:
    print(f"Failed to fetch token. Status code: {response.status_code}, Response: {response.text}")




