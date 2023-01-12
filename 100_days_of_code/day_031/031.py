# Day 31: Classic UI with f-string


def colour_text(colour: str, text: str) -> str:
    """Colour text in the specified colour."""
    colour = colour.lower()
    if colour == 'red':
        colour_number = 31
    elif colour == 'green':
        colour_number = 32
    elif colour == 'yellow':
        colour_number = 33
    elif colour == 'blue':
        colour_number = 34
    elif colour == 'purple':
        colour_number = 35
    elif colour == 'cyan':
        colour_number = 36
    else:  # white
        colour_number = 37
    return f'\033[{colour_number}m{text}\033[0m'


def ui_1() -> None:
    """Create the first user interface."""
    title_1 = (f"{colour_text('red', '=')}"
               f"{colour_text('white', '=')}"
               f"{colour_text('blue', '=')}")
    title_2 = colour_text('yellow', ' Music App ')
    title_3 = (f"{colour_text('blue', '=')}"
               f"{colour_text('white', '=')}"
               f"{colour_text('red', '=')}")
    print(f'{title_1 + title_2 + title_3: ^100}')
    print()
    print('\U0001F525 \U000025B6  Radio Gaga')
    print(f"{colour_text('yellow', 'Queen'): ^26}")
    print()
    word_dict = {'white': 'prev', 'green': 'next', 'purple': 'pause'}
    for key, value in word_dict.items():
        print(colour_text(key, value.upper() + '  '), end='\v')
    print()


def ui_2() -> None:
    """Create the second user interface."""
    title_1 = 'WELCOME TO'
    title_2 = '--   ARMBOOK   --'
    print(f'{title_1: ^40}',
          f"{colour_text('blue', title_2): ^50}",
          sep='\n',
          end='\n\n')
    text = 'Definitely not a rip off of'
    print(f"{colour_text('yellow', text): >50}")
    text = 'a certain other social'
    print(f"{colour_text('yellow', text): >50}")
    text = 'networking site'
    print(f"{colour_text('yellow', text): >50}")
    print()
    print(f"{colour_text('red', 'Honest.'): ^50}")
    print()
    print(f"{colour_text('white', 'Username:'): ^50}")
    print(f"{colour_text('white', 'Password:'): ^50}")
    print()


def main() -> None:
    ui_1()
    ui_2()


if __name__ == '__main__':
    main()
