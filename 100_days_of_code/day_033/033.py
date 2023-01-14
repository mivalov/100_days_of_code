# Day 33: To Do List Manager
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
        '\t- View the list',
        '\t- Add an item to the list',
        '\t- Remove an item from the list',
        '\t- Exit from the program',
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
        if menu == 'view':
            print_todo_list(todo_list)
            time.sleep(5)
        elif menu == 'add':
            elem = input('What do you want to add to your list?\n').strip()
            todo_list.append(elem)
        elif menu == 'remove':
            elem = input(
                'What do you want to remove from your list?\n').strip()
            if elem in todo_list:
                todo_list.remove(elem)
        elif menu in ['stop', 'exit', 'quit']:
            break
        else:
            print('Incorrect input! Try again ...')
        os.system('clear')


if __name__ == '__main__':
    main()
