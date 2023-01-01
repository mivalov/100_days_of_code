# Day 20: Number Generator

from itertools import cycle

msg = 'Number Generator'
print(msg, len(msg) * '=', sep='\n')

# colour table from day 4, except black for better readability
colour = cycle((col for col in range(31, 38)))

while True:
    try:
        start = int(input('Start at: '))
        end = int(input('End before: '))
        increment = int(input('Increment between values: '))
    except ValueError:
        print('Incorrect input! Try again..')
    else:
        if (start >= end and increment >= 0) \
                or (start <= end and increment <= 0):
            print(
                'Your input does not really make sense. Please try again. (:')
            continue
        for i in range(start, end, increment):
            print(f'\033[{next(colour)}m{i}\033[0m')
        break
