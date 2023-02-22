# Day 72: Private Diary
import os
import random
import time
from datetime import datetime
from getpass import getpass

from replit import db


def display_options() -> None:
    print(
        '1. Add',
        '2. View',
        '3. Exit',
        sep='\n',
        end='\n\n'
    )


def add_entry() -> None:
    time.sleep(1)
    os.system('clear')
    timestamp = datetime.now().strftime('%Y%m%d%H%M')
    timestamp = f'072_{timestamp}'
    entry = input(f'Diary entry for {timestamp}: ')
    db[timestamp] = entry


def view_entries() -> None:
    matching_keys = db.prefix('072_')
    for key in matching_keys:
        time.sleep(1)
        os.system('clear')
        print(f'{key}: {db.get(key)}\n')
        next_entry = input('Next or exit? ').lower()
        if next_entry != 'next':
            break


def main():
    # db.clear()
    title = 'Private Diary'
    print(title)
    keys = db.keys()
    print(f'{keys = }')
    for k in keys:
        print(f'{db.get(k) = }')
    if len(keys) == 0:
        print('This seems to be your first time here. '
              'You will need to create an account')
        username = input('Username: ').strip()
        password = getpass('Password: ')
        salt = random.randint(1, 999999)
        new_pass = hash(f'{password}{salt}')
        db[username] = {'password': new_pass, 'salt': salt}
    else:
        print('Log in')
        username = input('Username: ').strip()
        if username not in keys:
            print('Username does not exist')
            exit()
        password = getpass('Password: ')
        salt = db.get(username, {}).get('salt')
        new_pass = hash(f'{password}{salt}')
        if db.get(username, {}).get('password') != new_pass:
            print('Username or password is incorrect')
            exit()

    while True:
        os.system('clear')
        print(title)
        display_options()
        option = input('> ')
        if option == '1':
            add_entry()
        elif option == '2':
            view_entries()
        elif option == '3':
            break
        else:
            print('Incorrect option!')


if __name__ == '__main__':
    main()
