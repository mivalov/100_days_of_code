# Day 44: Bingo Game
import os
import random
import time
from typing import Any, List


def get_random_number(min_limit: int = 1, max_limit: int = 90) -> int:
    """Return a random integer between given limits."""
    return random.randint(min_limit, max_limit)


def display_bingo_card(bingo_card: List[List[Any]]) -> None:
    """Print a given list in a specific format."""
    print()
    # adjust it to the list index
    max_rows = len(bingo_card) - 1
    for i, row in enumerate(bingo_card):
        max_cols = len(row) - 1
        for j, col in enumerate(row):
            if j == 0:  # first element
                print(f'{col: >2} ', end='')
            elif j != max_cols:  # middle elements
                print(f'| {col: ^6}', end='')
            else:  # last element
                print(f'| {col: >2}', end='')
        if i != max_rows:
            print('\n', 15 * '-', sep='')
    print('\n')


def generate_bingo_card() -> List[List[Any]]:
    """Return a bingo card."""
    bingo_card = [
        [0, 0, 0],
        [0, 'BINGO', 0],
        [0, 0, 0],
    ]
    picked_numbers = []
    while len(picked_numbers) < 8:
        number = get_random_number()
        if number in picked_numbers:
            continue
        picked_numbers.append(number)
    picked_numbers.sort()
    counter = 0
    for r in range(3):
        for c in range(3):
            if not (r == 1 and r == c):
                bingo_card[r][c] = picked_numbers[counter]
                counter += 1
    return bingo_card


def main() -> None:
    msg = 'Bingo'
    bingo_card = generate_bingo_card()
    x_counter = 0
    while True:
        print(f'{msg: ^15}', 15 * '=', sep='\n')
        display_bingo_card(bingo_card)
        if x_counter >= 8:
            print('You have won!')
            break
        try:
            next_number = int(input('Next Number: '))
        except ValueError:
            print('Incorrect input! Please try again..')
            continue
        for row in range(3):
            for col in range(3):
                if bingo_card[row][col] == next_number:
                    bingo_card[row][col] = 'X'
                    x_counter += 1
        time.sleep(1)
        os.system('clear')


if __name__ == '__main__':
    main()
