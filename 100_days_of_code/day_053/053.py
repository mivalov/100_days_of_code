# Day 53: Video Game Inventory

import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Any


def load_data(file: Path) -> List[List[Any]]:
    """Load data from a file and return them in a list form."""
    data = []
    if file.exists() and file.is_file():
        # load data from file
        print(f'The file {file} exists. Loading data from file...')
        with open(file, 'r') as f_in:
            data = [row.strip() for row in f_in]
    elif file.is_dir():
        print(f'"{file}" is actually a directory!')
        utc_now = int(datetime.now(timezone.utc).timestamp())
        new_name = f'{file}_{utc_now}'
        file.rename(new_name)
        print(f'The directory "{file}" was renamed to "{new_name}".')
    else:
        print(f'The file {file} does not exist. It will be created later on.')
    return data


def store_data(file: Path, data: List[Any]) -> None:
    """Save data locally to a given file."""
    result = '\n'.join([item for item in data])
    with open(file, 'w') as f_out:
        f_out.write(result)


def print_menu() -> None:
    """Display the input options."""
    print('\t1. Add an item to the inventory',
          '\t2. Display item',
          '\t3. Remove item from the inventory',
          '\t4. Reset inventory',
          '\t5. Save items and exit',
          sep='\n')


def display_items(inventory: List[Any]) -> None:
    """Display the inventory."""
    print('Your inventory contains:')
    seen = []
    for item in inventory:
        if item not in seen:
            print(f'{item}: {inventory.count(item)}')
            seen.append(item)


def add_item(inventory: List[Any]) -> List[Any]:
    """Add an item to the list."""
    item = input('Item to add: ').capitalize()
    inventory.append(item)
    print('Added to inventory.')
    return inventory


def remove_item(inventory: List[Any]) -> List[Any]:
    """Remove an item from the list."""
    print()
    item = input('Item to remove: ').capitalize()
    if item in inventory:
        inventory.remove(item)
        print('Item removed.')
    else:
        print('The given item is missing.')
    return inventory


def main() -> None:
    msg = "🌟 RPG Inventory 🌟 "
    underline = len(msg) * '='
    file = Path('inventory.txt')
    inventory = load_data(file)
    time.sleep(1)
    os.system('clear')
    while True:
        print(msg, underline, sep='\n', end='\n\n')
        print_menu()
        menu = input()
        if menu == '1':
            add_item(inventory)
        elif menu == '2':
            display_items(inventory)
        elif menu == '3':
            remove_item(inventory)
        elif menu == '4':
            inventory = []
        elif menu == '5':
            break
        else:
            print('Incorrect option')
        time.sleep(1)
        os.system('clear')

    store_data(file, inventory)


if __name__ == '__main__':
    main()
