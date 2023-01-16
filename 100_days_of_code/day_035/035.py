# Day 35: To Do List Manager

import os
import time


def print_todo_list(todo_list: list) -> None:
    """Print out the contained elements within a given list."""
    print('\nYour To Do List:')
    for index, element in enumerate(todo_list):
        print(f'{index + 1}. {element}')
    print()


def print_menu() -> None:
    """Print out the possible actions that the program can accept."""
    print(
        'Possible Actions:',
        '\t1. View the list',
        '\t2. Add an item to the list',
        '\t3. Edit an item from the list',
        '\t4. Remove an item from the list',
        '\t5. Remove the whole list',
        '\t6. Exit from the program',
        sep='\n'
    )


def main() -> None:
    msg = 'To Do List Manager'
    underline = len(msg) * '='
    todo_list = []
    while True:
        print(msg, underline, sep='\n', end='\n\n')
        print_menu()
        menu = input().lower()
        if menu == '1':
            print_todo_list(todo_list)
            time.sleep(2)
        elif menu == '2':
            elem = input(
                'What do you want to add to your list?\n'
            ).strip().capitalize()
            if elem not in todo_list:
                todo_list.append(elem)
            else:
                print('Your item already exists in the list.')
        elif menu == '3':
            print_todo_list(todo_list)
            elem = input('What do you want to edit?\n').strip().capitalize()
            new_value = input(
                'What do you want to change it to?\n'
            ).strip().capitalize()
            for index, item in enumerate(todo_list):
                if item == elem:
                    todo_list[index] = new_value
            else:
                print('Your item does not exist in the list.')
        elif menu == '4':
            elem = input(
                'What do you want to remove from your list?\n'
            ).strip().capitalize()
            if elem in todo_list:
                double_check = input('Are you sure you want to remove this? ')
                if double_check.lower() == 'yes':
                    todo_list.remove(elem)
        elif menu == '5':
            todo_list = []
        elif menu == '6':
            break
        else:
            print('Incorrect input! Try again ...')
        os.system('clear')


if __name__ == '__main__':
    main()
