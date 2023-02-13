# Day 63: Library

def change_colour(colour: str) -> None:
    if colour == ' ':
        print('\033[0m', end='')
    elif colour == 'r':
        print('\033[31m', end='')
    elif colour == 'g':
        print('\033[32m', end='')
    elif colour == 'y':
        print('\033[33m', end='')
    elif colour == 'b':
        print('\033[34m', end='')
    elif colour == 'p':
        print('\033[35m', end='')


def main() -> None:
    change_colour('r')
    print('red')
    change_colour('g')
    print('green')
    change_colour(' ')


if __name__ == '__main__':
    main()
