# Day 62: Private Diary

import os
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
    timestamp = f'062_{timestamp}'
    entry = input(f'Diary entry for {timestamp}: ')
    db[timestamp] = entry


def view_entries() -> None:
    matching_keys = db.prefix('062')
    for key in matching_keys:
        time.sleep(1)
        os.system('clear')
        print(f'{key}: {db.get(key)}\n')
        next = input('Next or exit? ').lower()
        if next != 'next':
            break


def main():
    # db.clear()
    title = 'Private Diary\n'
    print(title)
    correct_pass = True
    stored_pass = db.get('p062_password')
    if stored_pass is None:
        db['p062_password'] = getpass('First-time password: ')
    else:
        print(db.get('p062_password'))
        password = getpass('Password: ')
        if password != db.get("p062_password"):
            print('Incorrect password')
            correct_pass = False
    while correct_pass:
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
