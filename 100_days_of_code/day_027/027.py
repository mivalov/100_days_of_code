# Day 27: Video Game (Part 1)
import os
import time
from random import randint


def roll_dice(sides: int = 6) -> int:
    """Return a value from an n-sided game die."""
    return randint(1, sides)


def gen_hp() -> int:
    """Generate health value using a formula."""
    return ((roll_dice(6) * roll_dice(12)) // 2) + 10


def gen_strength() -> int:
    """Generate strength value using a formula."""
    return ((roll_dice(6) * roll_dice(8)) // 2) + 12


def main() -> None:
    msg = '\U00002694 Character Builder \U00002694 '
    underline = len(msg) * '='
    accepted_ans = ['yes', 'ye', 'yeah', 'y']
    allowed_races = ['human', 'elf', 'tauren', 'orc']
    while True:
        print(msg, underline, sep='\n')
        time.sleep(1)
        legend_name = input('Name your Legend: \n')
        time.sleep(1)
        char_race = input(
            'Character Type (Human, Elf, Tauren, Orc): \n'
        ).strip().lower()
        if char_race not in allowed_races:
            print(
                "Your input was incorrect! "
                "You must choose one of the following: "
                "'Human', 'Elf', 'Tauren' or 'Orc'."
            )
            time.sleep(3)
            print('You must start over!\n')
            continue
        time.sleep(1)
        print('',
              f'NAME: {legend_name}',
              f'RACE: {char_race}',
              f'HEALTH: {gen_hp()}',
              f'STRENGTH: {gen_strength()}',
              '',
              'May your name go down in Legend...',
              '',
              sep='\n')
        time.sleep(1)
        again = input('Again? ').lower()
        if again in accepted_ans:
            os.system('clear')
            continue
        else:
            break


if __name__ == '__main__':
    main()
