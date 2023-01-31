# Day 50: Idea storage system

import os
import time
import random


def add(file: str) -> None:
    os.system('clear')
    idea = input('Write your idea: ')
    with open(file, 'a+') as f:
        f.write(f'{idea}\n')
    time.sleep(1)
    os.system('clear')


def show(file: str) -> None:
    os.system('clear')
    with open(file, 'r') as f:
        ideas = f.read().split('\n')
    ideas.remove('')
    ideas = list(set(ideas))
    idea = random.choice(ideas)
    print(idea)
    time.sleep(2)
    os.system('clear')


def main() -> None:
    print('Idea Storage System')
    msg = 'Menu:\n\t1. Add an idea\n\t2. See a random idea'
    file = 'my_ideas.txt'
    while True:
        print(msg)
        menu = input('')
        if menu == '1':
            add(file)
        elif menu == '2':
            show(file)
        else:
            print('Wrong input! Please try again..')
            time.sleep(1)


if __name__ == '__main__':
    main()
