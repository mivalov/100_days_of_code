# Day 10: Basic math principles

try:
    bill = float(input('How much did you spend? '))
    percentage = float(input('What percentage do you want to tip? '))
    number_of_people = int(input('How many people are in your group? '))
except ValueError:
    print('Your input is incorrect! You must enter numbers! Try again ...')
else:
    bill += bill * percentage / 100
    answer = round(bill / number_of_people, 2)
    print('Each one of you owes', answer, '€')
