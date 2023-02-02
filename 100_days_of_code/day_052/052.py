# Day 52: Dave's Amazing Pizzeria
import os
import time
from typing import List
from pathlib import Path


def print_menu() -> None:
    """Display the input options."""
    print('\t1. Add an order',
          '\t2. View orders',
          '\t3. Clear orders',
          '\t4. Save orders and exit',
          sep='\n')


def view_orders(orders: List) -> None:
    """Display the orders."""
    c1 = 'Name'
    c2 = 'Topping'
    c3 = 'Size'
    c4 = 'Quantity'
    c5 = 'Total'
    print(f'{c1: ^10}{c2: ^20}{c3: ^10}{c4: ^10}{c5: ^10}')
    for row in orders:
        print(f'{row[0]: ^10}{row[1]: ^20}{row[2]: ^10}'
              f'{row[3]: ^10}{row[4]: ^10}')


def add_order(orders: List) -> List:
    """Add an order to the list."""
    name = input('Name: ').capitalize()
    toppings = input('Toppings: ').lower()
    size = input('Size (s/m/l): ').lower()
    cost = 0
    quantity = 0
    while True:
        if size not in ['s', 'm', 'l']:
            print('Size must be small (s), medium (m) or large (l)')
            size = input('Size (s/m/l): ').lower()
            continue
        try:
            quantity = int(input('Quantity: '))
        except ValueError:
            print('Incorrect input! Please enter an integer.')
        else:
            if size == 's':
                cost = 6.99
            elif size == 'm':
                cost = 9.99
            elif size == 'l':
                cost = 14.99
            break
    total = cost * quantity
    total = round(total, 2)
    order = [name, toppings, size, quantity, total]
    orders.append(order)
    return orders


def main() -> None:
    msg = "🌟Dave's Amazing Pizzeria🌟 "
    underline = len(msg) * '='
    file = Path('orders.txt')
    orders = []
    if file.exists() and file.is_file():
        # load data from file
        print(f'The file {file} exists. Loading data from file...')
        with open(file, 'r') as f_in:
            orders = [row.strip().split(';') for row in f_in]
    else:
        print(f'The file {file} does not exist. It will be created later on.')
    time.sleep(1)
    os.system('clear')
    while True:
        print(msg, underline, sep='\n', end='\n\n')
        print_menu()
        menu = input()
        if menu == '1':
            time.sleep(1)
            os.system('clear')
            add_order(orders)
        elif menu == '2':
            view_orders(orders)
            time.sleep(2)
            os.system('clear')
        elif menu == '3':
            orders = []
        elif menu == '4':
            break
        else:
            print('Incorrect option')

        # save data to file
        result = '\n'.join(
            [';'.join([str(item) for item in row]) for row in orders])
        # print(f'{result = }')
        with open(file, 'w') as f_out:
            f_out.write(result)


if __name__ == '__main__':
    main()
