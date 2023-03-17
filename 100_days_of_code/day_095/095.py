# Day 95: API Mashup (Part2)

import os
from urllib.parse import urlsplit, urlencode, urlunsplit

import openai
import requests
from requests.auth import HTTPBasicAuth
from requests.models import Response


def build_news_request(news_api_key: str, country_code: str = 'us') -> str:
    """Generate a request to a news API for a given country code."""
    news_api = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=API_KEY'
    parts = urlsplit(news_api)
    query = {
        'country': country_code.lower(),
        'apiKey': news_api_key,
    }
    query = urlencode(query)
    return urlunsplit((
        parts.scheme, parts.netloc, parts.path, query, parts.fragment
    ))


def request_spotify_token(spotify_client_id: str,
                          spotify_client_secret: str) -> Response:
    token_url = 'https://accounts.spotify.com/api/token'
    data = {
        'grant_type': 'client_credentials'
    }
    auth = HTTPBasicAuth(spotify_client_id, spotify_client_secret)
    return requests.post(
        url=token_url,
        data=data,
        auth=auth
    )


def get_spotify_token(response: Response) -> str:
    """Parse response and extract authentication token."""
    response_json = response.json()
    access_token = response_json.get('access_token')
    token_type = response_json.get('token_type')
    return f'{token_type} {access_token}'


def build_spotify_url(headline: str) -> str:
    """Build a custom search url based on given text."""
    search_api = 'https://api.spotify.com/v1/search'
    parts = urlsplit(search_api)
    query = {
        'q': f'{headline}',
        'type': 'track'
    }
    query = urlencode(query)
    return urlunsplit((
        parts.scheme, parts.netloc, parts.path, query, parts.fragment
    ))


def main() -> None:
    max_counter = 10
    news_api_key = os.getenv('NEWS_API_KEY')
    openai.api_key = os.getenv('OPENAI_API_KEY')
    openai.organisation = os.getenv('OPENAI_ORGANISATION_ID')
    openai.Model.list()

    spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID')
    spotify_client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

    spotify_authorization_token = get_spotify_token(request_spotify_token(
        spotify_client_id, spotify_client_secret
    ))
    headers = {
        'Authorization': f'{spotify_authorization_token}'
    }

    country_code = 'gb'
    url = build_news_request(news_api_key, country_code)
    response = requests.get(url)
    response_json = response.json()
    articles = response_json.get('articles')

    openai_response_list = []
    spotify_songs = []

    counter = 0
    for article in articles:
        counter += 1
        if counter > max_counter:
            break
        prompt = f"Summarise {article.get('url')} in up to 4 words."
        openai_response = openai.Completion.create(
            model='text-davinci-002',
            prompt=prompt,
            temperature=0,
            max_tokens=20
        )
        # print(openai_response.get('choices')[0].get('text').strip())
        openai_response_list.append(
            openai_response.get('choices')[0].get('text').strip())

    for headline in openai_response_list:
        spotify_response = requests.get(
            url=build_spotify_url(headline),
            headers=headers
        )
        spotify_json_response = spotify_response.json()
        try:
            spotify_songs.append(spotify_json_response.get(
                'tracks', {}).get('items', [])[0])
        except IndexError:
            spotify_songs.append({'name': None, 'preview_url': None})

    for i in range(max_counter):
        if spotify_songs[i].get('name') is not None:
            print(openai_response_list[i])
            print(spotify_songs[i].get('name'))
            print(spotify_songs[i].get('preview_url'))
            print()


if __name__ == '__main__':
    main()
