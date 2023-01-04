# Day 23: Functions

from getpass import getpass


def login() -> None:
    while True:
        username = input('What is your username? ')
        password = getpass('What is your password? ')
        if username == 'john' and password == 'securePassword':
            print('Welcome John!')
            break
        else:
            print('Incorrect username or password. Try again! (:')
            continue


def main() -> None:
    msg = 'Replit Login System'
    print(msg, len(msg) * '=', sep='\n')
    login()


if __name__ == '__main__':
    main()
