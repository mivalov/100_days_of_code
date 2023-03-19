# Day 97: Summarise anything
import os

import openai
import requests
from bs4 import BeautifulSoup


def get_wiki(url: str) -> str:
    """Return a wikipedia response in text format."""
    response = requests.get(url)
    return response.text


def main():
    url = 'https://en.wikipedia.org/wiki/Hair_loss'
    html = BeautifulSoup(get_wiki(url), 'html.parser')
    try:
        article = html.find_all(
            'div',
            {'class': 'mw-parser-output'}
        )[1]
    except IndexError:
        print('IndexError while parsing the article.')
    else:
        # print(f'{len(article) = }')

        # get paragraphs without any class
        p_tags = article.find_all('p', {'class': False})
        text = ''
        for p in p_tags:
            text += p.text

        # get references
        refs = html.find_all('ol', {'class': 'references'})
        references = ''
        for ref in refs:
            references += ref.text.replace('^ ', '')

        # openai auth
        openai.api_key = os.getenv('OPENAI_API_KEY')
        openai.organization = os.getenv('OPENAI_ORGANISATION_ID')
        openai.Model.list()

        prompt = f'Summarise the text below in up to 3 paragraphs. {text}'
        openai_response = openai.Completion.create(
            model='text-davinci-002',
            prompt=prompt,
            temperature=0,
            max_tokens=150
        )
        print(openai_response.get('choices')[0].get('text').strip())


if __name__ == '__main__':
    main()
