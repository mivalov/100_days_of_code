# Day 42: MokeBeasts (Part 2) - Mokedex
import os
import time


def change_colour(beast_type: str) -> None:
    """Change text colour based on beast type."""
    if beast_type == 'Fire':
        print('\033[31m', end='')
    elif beast_type == 'Air':
        print('\033[37m', end='')
    elif beast_type == 'Water':
        print('\033[34m', end='')
    elif beast_type == 'Earth':
        print('\033[33m', end='')
    else:
        print('\033[35m', end='')


def pretty_print(beasts: dict) -> None:
    """Display a table of stored beasts."""
    print(f'{"Name": ^15}|{"Type": ^11}|{"HP": ^6}|{"MP": ^6}')
    for name, props in beasts.items():
        change_colour(props.get('Type'))
        print(f'{name: ^15}|{props.get("Type"): ^11}|'
              f'{props.get("HP"): ^6}|{props.get("MP"): ^6}')
        print('\033[0m', end='')
    print()


def add_beast(moke_dex: dict) -> dict:
    """Add a beast to the MokeDex."""
    print('Add your Beast!')
    name = input('Beast name: ').capitalize()
    beast = {
        'Type': input('Type: ').capitalize(),
        'HP': input('HP: '),
        'MP': input('MP: '),
    }
    print(10 * '-', end='\n')
    moke_dex[name] = beast
    return moke_dex


def main() -> None:
    msg = 'MokèBeasts Full-on MokèDex'
    underline = len(msg) * '='
    moke_dex = {}
    positive_answer = ['yes', 'yeah', 'yep', 'y']
    while True:
        os.system('clear')
        print(msg, underline, sep='\n', end='\n\n')
        moke_dex = add_beast(moke_dex)
        pretty_print(moke_dex)
        again = input('Do you want to add another beast? ')
        if again not in positive_answer:
            break
        time.sleep(1)


if __name__ == '__main__':
    main()
