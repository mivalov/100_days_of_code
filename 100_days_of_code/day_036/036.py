# Day 36: String Manipulation

def print_list(list_name: list) -> None:
    print()
    for item in list_name:
        print(item)
    print()


def main() -> None:
    names = []
    while True:
        first_name = input('First name: ').strip().capitalize()
        last_name = input('Last name: ').strip().capitalize()
        name = f'{first_name} {last_name}'
        if name not in names:
            names.append(name)
            print_list(names)
        else:
            print('Error: You have entered a duplicate.')
            continue
        again = input('Do you want to continue? ').strip().lower()
        print()
        if again not in ['yes', 'y']:
            break


if __name__ == '__main__':
    main()
