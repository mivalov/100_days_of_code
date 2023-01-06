# Day 25: Character Stats Generator

from random import randint


def roll_dice(sides: int = 6) -> int:
    return randint(1, sides)


def generate_hp():
    """Generate health by multiplying 6- and 8-sided dice rolls."""
    roll_d1 = roll_dice(6)
    roll_d2 = roll_dice(8)
    return roll_d1 * roll_d2


def main() -> None:
    print('\U00002694 Character stats generator \U00002694')
    while True:
        character = input('Name your warrior: ')
        health = generate_hp()
        print(f"{character}'s health is {health} hp.")
        another_character = input('Do you want to create another character? ')
        if another_character.lower() not in ['yes', 'yeah', 'y']:
            break


if __name__ == '__main__':
    main()
