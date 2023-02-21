# Day 71: Pass the Salt
from getpass import getpass
import os
import time
import random

from replit import db


def create_user():
    time.sleep(1)
    os.system('clear')
    user = input('Username: ').strip()
    password = getpass('Password: ')
    keys = db.keys()
    if user in keys:
        print('Error: The given username already exists')
        return

    salt = random.randint(1000, 9999)
    new_pass = f'{password}{salt}'
    new_pass = hash(new_pass)

    db[user] = {'password': new_pass, 'salt': salt}
    print('The user has been successfully added!')


def login():
    time.sleep(1)
    os.system('clear')
    user = input('Username: ').strip()
    password = getpass('Password: ')
    keys = db.keys()
    if user not in keys:
        print('Error: The given username does not exist!')
        return

    salt = db.get(user, {}).get('salt')
    new_pass = f'{password}{salt}'
    new_pass = hash(new_pass)

    if db.get(user, {}).get('password') == new_pass:
        print('Successfully logged in')
        print(f'Welcome {user}')
    else:
        print('Username or password is incorrect')


def main() -> None:
    msg = '🌟Login System🌟'
    menu = '1. New User\n2. Login\n3. Exit'
    while True:
        print(msg, menu, sep='\n\n', end='\n\n')
        choice = input().strip()
        if choice == '1':
            create_user()
        elif choice == '2':
            login()
        else:
            # keys = db.keys()
            # for key in keys:
            #     print(db.get(key))
            break


if __name__ == '__main__':
    main()
