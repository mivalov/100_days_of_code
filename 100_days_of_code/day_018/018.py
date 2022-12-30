# Day 18: Guess the Number

import random

MIN_LIMIT = 0
MAX_LIMIT = 1_000_000
msg = f'Guess the Number (between {MIN_LIMIT} and {MAX_LIMIT})'
print(msg, len(msg) * '=', sep='\n')

secret_number = random.randint(MIN_LIMIT, MAX_LIMIT)
attempts = 0
while True:
    try:
        guess = int(input('What is your guess? '))
    except ValueError:
        print('Incorrect input! Try again..')
        continue
    else:
        attempts += 1
        if guess < MIN_LIMIT or guess > MAX_LIMIT:
            print(f'Your input must be between {MIN_LIMIT} and {MAX_LIMIT}.')
        elif guess == secret_number:
            print(
                f'You win! \U0001f389 It took you only '
                f'{attempts} attempts to get the correct answer!'
            )
            break
        elif guess > secret_number:
            print('Your guess is too high. Pick \U0001f53d')
        else:
            print('Your guess is too low. Pick \U0001f53c')
