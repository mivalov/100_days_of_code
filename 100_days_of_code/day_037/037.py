# Day 37: Star Wars Name Generator
import os
import time


def main() -> None:
    msg = '🌟 Star Wars Name Generator 🌟  '
    underline = len(msg) * '='
    msg2 = """Enter the following (separate each value by a comma):
    - First name
    - Last name
    - Mom's maiden name
    - City you were born in"""
    while True:
        print(msg, underline, sep='\n')
        print(msg2)
        inputs = input().strip().lower().split(',')
        inputs = [elem.strip() for elem in inputs]
        if len(inputs) == 4:
            first_name, last_name, mom, city = inputs
        else:
            print('Error! Try again next time.')
            time.sleep(1)
            os.system('clear')
            continue
        name = f'{first_name[:3]}{last_name[:3]} {mom[:2]}{city[-3:]}'
        name = name.title()
        print(f'Your Start Wars name is \033[32m{name}\033[0m')
        break


if __name__ == '__main__':
    main()
