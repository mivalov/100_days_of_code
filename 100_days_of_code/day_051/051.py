# Day 51: Improved To-Do List Management System

import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


def display_menu() -> None:
    """Display the menu options in the console."""
    print('',
          '1: Add Task',
          '2: View Tasks',
          '3: Edit Task',
          '4: Remove Task',
          '5: Reset List',
          '6: Exit Program',
          sep='\n',
          end='\n\n')


def add(todo_list: list) -> list:
    """Append an item to a to-do list and return it."""
    time.sleep(1)
    os.system('clear')
    name = input('Task name: ')
    date = input('Due date: ')
    priority = input('Priority: ').capitalize()
    row = [name, date, priority]
    todo_list.append(row)
    print('The task has been added.')
    time.sleep(1)
    return todo_list


def view(todo_list: list, option: Optional[str] = None) -> None:
    """Display the contents of a given to-do list."""
    time.sleep(1)
    os.system('clear')
    if option is None:
        print('View:', '\t1: All', '\t2: By Priority', sep='\n', end='\n\n')
        option = input()
    if option == '1':
        print('ToDo List:')
        for row in todo_list:
            for elem in row:
                print(elem, end=' | ')
            print()
        print()
    else:
        priority = input('What priority? ').capitalize()
        print(f'ToDo List with "{priority}" priority:')
        for row in todo_list:
            if priority in row:
                for elem in row:
                    print(elem, end=' | ')
                print()
        print()
    time.sleep(1)


def edit(todo_list: list) -> list:
    """Overwrite an existing task and return the new list."""
    time.sleep(1)
    os.system('clear')
    view(todo_list, '1')
    to_edit = input('Which task do you want to edit? ')
    found = None
    for i, row in enumerate(todo_list):
        if to_edit in row:
            found = i
    if found is None:
        print('Your task was not found ):')
        return todo_list
    name = input('Task name: ')
    date = input('Due date: ')
    priority = input('Priority: ').capitalize()
    todo_list[found] = [name, date, priority]
    print('The task has been updated.')
    time.sleep(1)
    return todo_list


def remove(todo_list: list) -> list:
    """Remove a certain task from a given list."""
    time.sleep(1)
    os.system('clear')
    view(todo_list, '1')
    to_remove = input('Which task do you want to remove? ')
    for row in todo_list:
        if to_remove in row:
            todo_list.remove(row)
            print(f'Removed task: {"; ".join(row)}')
    time.sleep(1)
    return todo_list


def main() -> None:
    msg = 'ToDo List Management System'
    underline = len(msg) * '='
    todo_list = []
    file = Path('todo.txt')
    if file.exists() and file.is_file():
        # load data from file
        print(f'The file {file} exists. Loading data from file...')
        with open(file, 'r') as f_in:
            todo_list = [row.strip().split(';') for row in f_in]
            # print(f'{todo_list = }')
    elif file.is_dir():
        print(f'"{file}" is actually a directory!')
        utc_now = int(datetime.now(timezone.utc).timestamp())
        new_name = f'{file}_{utc_now}'
        file.rename(new_name)
        print(f'The directory "{file}" was renamed to "{new_name}".')
    else:
        print(f'The file {file} does not exist. It will be created later on.')
    time.sleep(1)
    os.system('clear')

    while True:
        print(msg, underline, sep='\n')
        display_menu()
        menu = input()
        if menu == '1':
            todo_list = add(todo_list)
        elif menu == '2':
            view(todo_list)
        elif menu == '3':
            todo_list = edit(todo_list)
        elif menu == '4':
            remove(todo_list)
        elif menu == '5':
            todo_list = []
        elif menu == '6':
            break
        else:
            print('Incorrect option!')
        time.sleep(1)
        os.system('clear')

    # save data to file
    result = '\n'.join(
        [';'.join([str(item) for item in row]) for row in todo_list])
    # print(f'{result = }')
    with open(file, 'w') as f_out:
        f_out.write(result)


if __name__ == '__main__':
    main()
