# Day 18: Guess the Number (Part 2)

import random


def game(secret_number: int, min_limit: int, max_limit: int) -> None:
    msg = 'The game has started!'
    print(len(msg) * '-', msg, len(msg) * '-', sep='\n')
    print(f'Guess the number between {min_limit:,} and {max_limit:,}')
    attempt_counter = 0
    while True:
        try:
            guess = int(input('What is your guess? '))
        except ValueError:
            print('Incorrect input! You must enter a number...')
            continue
        else:
            attempt_counter += 1
            if guess < min_limit or guess > max_limit:
                print(
                    f'Your input must be between {min_limit:,} '
                    f'and {max_limit:,}.'
                )
            elif guess == secret_number:
                print(
                    f'You win! \U0001f389 It took you only '
                    f'{attempt_counter:,} attempts to get the correct answer!'
                )
                break
            elif guess > secret_number:
                print('Your guess is \033[31mtoo high\033[0m. Pick \U0001f53d')
            else:
                print('Your guess is \033[34mtoo low\033[0m. Pick \U0001f53c')


def main() -> None:
    msg = f'Guess the Number'
    print(msg, len(msg) * '=', sep='\n')
    try:
        min_limit = int(input('Enter the lower limit: '))
        max_limit = int(input('Enter the upper limit: '))
    except ValueError:
        print('Incorrect input!')
    else:
        if min_limit < max_limit:
            secret_number = random.randint(min_limit, max_limit)
            game(secret_number, min_limit, max_limit)
        elif min_limit > max_limit:
            min_limit, max_limit = max_limit, min_limit
            secret_number = random.randint(min_limit, max_limit)
            game(secret_number, min_limit, max_limit)
        else:
            print('Your input does not really make sense.')


if __name__ == '__main__':
    main()
