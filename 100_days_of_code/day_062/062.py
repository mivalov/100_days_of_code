# Day 62: Private Diary

from replit import db
from datetime import datetime
from getpass import getpass
import os
import time


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
    matching_keys = db.prefix('062_')
    for key in matching_keys:
        time.sleep(1)
        os.system('clear')
        print(f'{key}: {db.get("key")}\n')
        next = input('Next or exit? ').lower()
        if next != 'next':
            break


def main():
    db.clear()
    title = 'Private Diary'
    print(title)
    stored_pass = db.get('062_password')
    if stored_pass is None:
        db['062_password'] = getpass('First-time password: ')
    else:
        print(db.get('062_password'))
        password = getpass('Password: ')
        if password != db.get("062_password"):
            print('Incorrect password')
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
