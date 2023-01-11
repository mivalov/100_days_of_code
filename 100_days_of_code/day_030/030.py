# Day 30: f-strings

def main() -> None:
    print('30 Days Down - What did you think?', end='\n\n')
    for day in range(1, 31):
        msg = f'You thought Day {day} was'
        opinion = input(f'Day {day}:\n')
        print()
        print(f'{msg: ^40}')
        print(f'{opinion: ^40}')


if __name__ == '__main__':
    main()
