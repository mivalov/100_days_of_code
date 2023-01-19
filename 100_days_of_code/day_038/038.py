# Day 38: Code the Rainbow

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
    sentence = input('What sentence do you want rainbow-ising?\n').strip()
    for letter in sentence:
        change_colour(letter.lower())
        print(letter, end='')


if __name__ == '__main__':
    main()
