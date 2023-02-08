# Day 58: Debugging

import random


def game():
    attempts = 0
    number = random.randint(1, 100)
    while True:
        guess = int(input('Pick a number between 1 and 100: '))
        if guess > number:
            print('Too high')
            attempts += 1
        elif guess < number:
            print('Too low')
            attempts += 1
        else:
            print('Just right!')
            print(f'{attempts} attempts this round')
            return attempts


def display_menu() -> None:
    """Print out the menu in the console."""
    print(
        '1: Guess the random number game',
        '2: Total Score',
        '3: Exit',
        sep='\n'
    )


def main() -> None:
    total_attempts = 0
    while True:
        display_menu()
        menu = input('> ')
        if menu == '1':
            total_attempts += game()
        elif menu == '2':
            print(f"You've had {total_attempts} attempts.")
        else:
            break


if __name__ == '__main__':
    main()
