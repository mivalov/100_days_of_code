# Day 29: Print

def print_with_colour(word: str, colour: str) -> None:
    if colour == 'red':
        colour_number = 31
    elif colour == 'green':
        colour_number = 32
    elif colour == 'yellow':
        colour_number = 33
    elif colour == 'blue':
        colour_number = 34
    else:
        colour_number = 0
    print(f'\033[{colour_number}m{word}\033[0m', sep='', end='')


def main() -> None:
    print('Super Subroutine', end='\n\n')
    print('With my ', end='')
    print_with_colour('new program', 'green')
    print(' I can just call red("and") ', end='')
    print_with_colour('and', 'red')
    print(' that word will appear in the colour I set it to.', end='\n\n')
    print('With no ', end='')
    print_with_colour('weird gaps', 'blue')
    print('.', end='\n\n')
    print('Epic.')


if __name__ == '__main__':
    main()
