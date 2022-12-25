# Day 13: Grade Calculator

print('Grade Calculator')
print(16 * '=')

exam_name = input('Name of the exam: ')
try:
    max_score = float(input('Max. Possible Score: '))
    score = float(input('Your score: '))
except ValueError:
    print('Wrong input! Next time enter digits...')
else:
    result = (score / max_score) * 100
    result = round(result, 2)
    def_colour = '\033[0m'
    colour = '\033[32m'
    if result >= 96:
        grade = 'A+'
    elif result >= 90:
        grade = 'A'
    elif result >= 80:
        grade = 'A-'
    elif result >= 70:
        grade = 'B'
        colour = '\033[33m'
    elif result >= 60:
        grade = 'C'
        colour = '\033[33m'
    elif result >= 50:
        grade = 'D'
        colour = '\033[33m'
    else:
        grade = 'F'
        colour = '\033[31m'
    print(
        f'On your exam in \033[34m"{exam_name}"{def_colour} '
        f'you got {colour}{result}%{def_colour} which means '
        f'that your grade is {colour}{grade}{def_colour}.')
