# Day 34: Pretty printing

import os
import time


def pretty_print(list_of_emails: list) -> None:
    os.system('clear')
    print('list_of_emails')
    print()
    counter = 1
    for order in list_of_emails:
        print(f'{counter}: {order}')
        counter += 1
    time.sleep(1)


def spam(max_emails: int, list_of_emails: list) -> None:
    if max_emails > len(list_of_emails):
        max_emails = len(list_of_emails)
    for email in range(max_emails):
        print(
            f"""Email {email + 1}
Dear {list_of_emails[email]}
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,
Ian Spammington III"""
        )
        time.sleep(2)
        os.system('clear')


def main() -> None:
    list_of_emails = []
    msg = 'SPAMMER Inc.'
    underline = len(msg) * '='
    while True:
        print(
            msg, underline, '',
            '1. Add email',
            '2: Remove Email',
            '3. Show emails',
            '4. Get SPAMMING',
            '5. Exit',
            sep='\n'
        )
        menu = input('> ')
        if menu == '1':
            email = input('Email > ')
            list_of_emails.append(email)
        elif menu == '2':
            email = input('delete email> ')
            if email in list_of_emails:
                list_of_emails.remove(email)
        elif menu == '3':
            pretty_print(list_of_emails)
        elif menu == '4':
            spam(10, list_of_emails)
        elif menu == '5':
            break
        time.sleep(1)
        os.system('clear')


if __name__ == '__main__':
    main()
