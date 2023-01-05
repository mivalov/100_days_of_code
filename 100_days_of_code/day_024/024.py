# Day 24: Roll a dice

from random import randint


def roll_dice(sides: int = 6) -> None:
    msg = f'The game has started and your dice has {sides} sides.'
    print(msg, len(msg) * '-', sep='\n')
    while True:
        print(f'You rolled {randint(1, sides)}')
        play_again = input('Roll again? ').lower()
        if play_again not in ['yes', 'yeah', 'y']:
            break


def main() -> None:
    print('Infinity Dice \U0001F3B2')

    try:
        sides = int(input('How many sides? '))
    except ValueError:
        print('Incorrect input')
    else:
        if sides > 0:
            roll_dice(sides)
        else:
            print('Incorrect input')


if __name__ == '__main__':
    main()
