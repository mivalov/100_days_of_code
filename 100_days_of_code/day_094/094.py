# Day 94: API Mashup

import os
from urllib.parse import urlsplit, urlencode, urlunsplit

import openai
import requests


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


def main() -> None:
    news_api_key = os.getenv('NEWS_API_KEY')
    openai.api_key = os.getenv('OPENAI_API_KEY')
    openai.organisation = os.getenv('OPENAI_ORGANISATION_ID')
    openai.Model.list()

    country_code = 'gb'
    url = build_news_request(news_api_key, country_code)
    response = requests.get(url)
    response_json = response.json()
    articles = response_json.get('articles')
    counter = 0
    for article in articles:
        counter += 1
        if counter > 5:
            break
        prompt = f"Summarise {article.get('url')} in one sentence."
        openai_response = openai.Completion.create(
            model='text-davinci-002',
            prompt=prompt,
            temperature=0,
            max_tokens=20
        )
        print(openai_response.get('choices')[0].get('text').strip())


if __name__ == '__main__':
    main()
