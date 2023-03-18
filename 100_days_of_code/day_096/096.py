# Day 96: Let's get scraping

from bs4 import BeautifulSoup
import requests


def main() -> None:
    keywords = ['replit', 'python', 'github',
                'aws', 'microsoft', 'youtube', ]
    url = 'https://news.ycombinator.com/'

    response = requests.get(url)
    response_html = response.text
    parsed_html = BeautifulSoup(markup=response_html, features='html.parser')
    links = parsed_html.find_all('span', {'class': 'titleline'})
    # print(f'{links = }')
    for link in links:
        to_display = False
        text = link.get_text()
        word_list = text.split()
        # print(f'{word_list = }')
        for word in word_list:
            if word.lower() in keywords:
                # print(f'{word = }')
                to_display = True
                break
        if to_display:
            hyperlink = link.find('a')['href']
            # print(f'{link = }')
            print(f'{text}')
            print(f'{hyperlink}')
            print()


if __name__ == '__main__':
    main()
