# Day 28: Video Game (Part 2)

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


def print_stats(char_name: str, char_race: str,
                char_hp: int, char_strength: int) -> None:
    print('',
          char_name,
          f'RACE: {char_race}',
          f'HEALTH: {char_hp}',
          f'STRENGTH: {char_strength}',
          sep='\n')


def print_hp(char_name: str, char_hp: int) -> None:
    print('', char_name, f'HEALTH: {char_hp}', sep='\n')


def main() -> None:
    msg = '\U00002694 Battle Time \U00002694 '
    underline = len(msg) * '='
    print(msg, underline, sep='\n')
    c1_name = input('Name your legend:\n')
    c1_race = input('Character race (Human, Elf, Tauren, Orc):\n')
    c1_hp = gen_hp()
    c1_strength = gen_strength()
    print_stats(c1_name, c1_race, c1_hp, c1_strength)
    time.sleep(1)
    print()
    print('Who are they battling?')
    print()
    c2_name = input('Name your legend:\n')
    c2_race = input('Character race (Human, Elf, Tauren, Orc):\n')
    c2_hp = gen_hp()
    c2_strength = gen_strength()
    print_stats(c2_name, c2_race, c2_hp, c2_strength)
    strength_diff = abs(c1_strength - c2_strength) + 1
    round_counter = 1
    while True:
        time.sleep(2)
        os.system('clear')
        print(msg, underline, '', sep='\n')

        if round_counter == 1:
            print('The battle begins!')
        else:
            print('The battle continues!')

        c1_roll = roll_dice(6)
        c2_roll = roll_dice(6)
        if c1_roll > c2_roll:
            c2_hp -= strength_diff
            if round_counter == 1:
                print(f'{c1_name} takes the first blood!')
            else:
                print(f'{c1_name} wins round {round_counter}')

        elif c1_roll < c2_roll:
            c1_hp -= strength_diff
            if round_counter == 1:
                print(f'{c2_name} takes the first blood!')
            else:
                print(f'{c2_name} wins round {round_counter}')
        else:
            print(f'Round {round_counter} ends up in draw')

        print_hp(c1_name, c1_hp)
        print_hp(c2_name, c2_hp)
        print()

        if c1_hp <= 0:
            print(f'{c1_name} has died!')
            winner = c2_name
            loser = c1_name
            break
        elif c2_hp <= 0:
            print(f'{c2_name} has died!')
            winner = c1_name
            loser = c2_name
            break
        else:
            print('Both warriors are still standing for the next round')
            round_counter += 1

    time.sleep(2)
    os.system('clear')
    print(msg, underline, sep='\n')
    print(f'{winner} destroyed {loser} in {round_counter} rounds!')


if __name__ == '__main__':
    main()
