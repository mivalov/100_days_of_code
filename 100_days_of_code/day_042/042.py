# Day 42: Moke Beasts

def main() -> None:
    beasts = {
        'name': None,
        'type': None,
        'special move': None,
        'starting HP': None,
        'starting MP': None
    }
    for key in beasts.keys():
        beasts[key] = input(f"Input your beast's {key}: ").strip().lower()

    if beasts.get('type') == 'fire':
        print('\033[31m', end='')
    elif beasts.get('type') == 'air':
        print('\033[37m', end='')
    elif beasts.get('type') == 'water':
        print('\033[34m', end='')
    elif beasts.get('type') == 'earth':
        print('\033[33m', end='')
    else:
        print('\033[35m', end='')
    print(
        f"Your beast ist called {beasts.get('name')}. "
        f"It is an {beasts.get('type')} beast "
        f"with a special move of {beasts.get('special move')}"
    )
    print('\033[0m', end='')


if __name__ == '__main__':
    main()
