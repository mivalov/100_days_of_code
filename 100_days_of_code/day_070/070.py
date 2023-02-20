# Day 70: Login System
# 1st a secret needs to be set
# in replit it is as if you add an env variable

from os import environ
from getpass import getpass


def main() -> None:
    msg = '🌟Login System🌟\n'
    print(msg)
    while True:
        user = input('Username: ').strip().lower()
        password = getpass('Password: ')
        if user == environ.get('ADMIN_USER') \
                and password == environ.get('ADMIN_PASS'):
            print('Welcome Admin')
            break
        elif user == environ.get('NORMIE_USER') \
                and password == environ.get('NORMIE_PASS'):
            print('Welcome Normy')
            break
        else:
            print('Better luck next time!')
        again = input('Again? ').strip().lower()
        if again not in ['yes', 'y']:
            break


if __name__ == '__main__':
    main()
