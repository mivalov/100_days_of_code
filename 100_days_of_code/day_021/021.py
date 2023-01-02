# Day 21: Math Game

from random import choice

msg = 'Math Game'
print(msg, len(msg) * '=', sep='\n')

positive_response = [
    'Great work!', 'Awesome!', 'Good job!', 'Fantastic job!',
    'You sure know your math!', 'Keep up the great work!'
]

try:
    multiple = int(input('Enter your multiple: '))
except ValueError:
    print('Incorrect input!')
else:
    score = 0
    for i in range(1, 11):
        result = i * multiple
        try:
            x = int(input(f'{i} x {multiple} = '))
        except ValueError:
            print('Incorrect input!')
        else:
            if x == result:
                score += 1
                print(choice(positive_response))
            else:
                print(f'Nope. The answer is {result}.')

    print('---')
    if score == 10:
        print('\U0001F3C6 A+ for your perfect math skills! \U0001F3C6')
    else:
        print(f'You scored {score} out of 10. ')
