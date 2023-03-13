# Day 91: The Joke's on You!
import os
import time

import requests
from replit import db


def get_random_joke(url: str = 'https://icanhazdadjoke.com/') -> dict:
    """Request a random joke from given API and return it.

    API documentation: https://icanhazdadjoke.com/api
    It requires HTTP header: Accept -> 'application/json'
    """
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'{url} returns HTTP status code: {response.status_code}')
        return {}


def main() -> None:
    while True:
        time.sleep(1)
        os.system('clear')
        joke_data = get_random_joke()
        joke = joke_data.get('joke', '')
        if joke == '':
            break  # end loop on unexpected response
        joke_id = joke_data.get('id', '')
        print(joke, end='\n\n')
        answer = input(
            '(s)ave joke, (l)oad old jokes, (n)ew joke\n> '
        ).strip().lower()
        if answer == 's':
            db[joke_id] = joke
            print('\nSaved\n')
        elif answer == 'l':
            keys = db.keys()
            for key in keys:
                print(db.get(key), end='\n\n')
                time.sleep(1)
        elif answer == 'n':
            continue
        elif answer == 'c':
            # secret feature: delete everything stored in the database
            db.clear()
        else:
            print('Incorrect input! Exiting the program.')
            break


if __name__ == '__main__':
    main()
