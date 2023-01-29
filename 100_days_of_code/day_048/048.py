# Day 40: Append to file

import os
import time

msg = '🌟HIGH SCORE TABLE🌟'
file_name = 'high.score'
accepted_answer = ['yes', 'ye', 'y', 'yeah']
while True:
    print(msg, end='\n\n')
    initials = input('Input your initials: ').upper()
    score = input('Input your score: ')
    print()

    with open(file_name, 'a+') as f_in:
        f_in.write(f'{initials} {score} \n')
    print('Added to high score table.\n')
    again = input('Add another (y/n)? ')
    if again not in accepted_answer:
        break
    time.sleep(2)
    os.system('clear')
