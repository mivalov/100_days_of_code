# Day 93: Spotify API - What's Your Top Ten?
import os
from urllib.parse import urlsplit, urlencode, urlunsplit

import requests
from flask import Flask, request
from replit import db
from requests.auth import HTTPBasicAuth

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

app = Flask(__name__, static_folder='static', template_folder='templates')


def request_token() -> requests.models.Response:
    token_url = 'https://accounts.spotify.com/api/token'
    data = {
        'grant_type': 'client_credentials'
    }
    auth = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    return requests.post(
        url=token_url,
        data=data,
        auth=auth
    )


def get_token(response: requests.models.Response) -> str:
    """Parse response and extract authentication token."""
    response_json = response.json()
    access_token = response_json.get('access_token')
    token_type = response_json.get('token_type')
    return f'{token_type} {access_token}'


def build_search_url(year: str = '1990', offset: int = 0) -> str:
    """Build a custom search url based on given year and offset."""
    search_api = 'https://api.spotify.com/v1/search'
    parts = urlsplit(search_api)
    offset = db.get(year)
    if offset >= 0:
        if offset >= 200:
            db[year] = 0
        db[year] += 10
    query = {
        'q': f'year:{year}',
        'type': 'track',
        'limit': 10,
        'offset': offset
    }
    query = urlencode(query)
    return urlunsplit((
        parts.scheme, parts.netloc, parts.path, query, parts.fragment
    ))


def get_top_songs(year: str) -> str:
    authorization_token = get_token(request_token())
    headers = {
        'Authorization': f'{authorization_token}'
    }

    response = requests.get(url=build_search_url(year), headers=headers)
    json_data = response.json()
    tracks = json_data.get('tracks', {}).get('items')
    with open('templates/songs.html', 'r') as file:
        page = file.read()

    song_list = ''
    for track in tracks:
        current_track = page
        name = f"{track.get('name')} by {track.get('artists')[0].get('name')}"
        current_track = current_track.replace('{name}', name)
        preview_url = f"{track.get('preview_url')}"
        current_track = current_track.replace('{url}', preview_url)
        song_list += current_track
    return song_list


# Flask part
@app.route('/')
def index():
    with open('templates/index.html', 'r') as file:
        page = file.read()
        page = page.replace('{songs}', '')
        page = page.replace('{year}', '1990')
    return page


@app.route('/', methods=['POST'])
def update():
    with open('templates/index.html', 'r') as file:
        page = file.read()
    year = request.form.get('year')
    songs = get_top_songs(year)
    page = page.replace('{songs}', songs)
    page = page.replace('{year}', year)
    return page


app.run(host='0.0.0.0', port=5000)

# this is to fix the replit db..
# def main():
#   keys = db.keys()
#   for key in keys:
#     print(f'{key}: {db.get(key)}')

#   # for year in range(1990, 2024):
#   #   db[year] = 0
#   # db.clear()

# if __name__ == '__main__':
#   main()
