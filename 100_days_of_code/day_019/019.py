# Day 19: Loan Calculator

import locale

locale.setlocale(locale.LC_ALL, '')

msg = 'Loan Calculator'
print(msg, len(msg) * '=', sep='\n')
print('Example: a loan of $1,000 with a 5% APR over 10 years.\n')

try:
    money_borrowed = float(input('Enter the amount of money you borrowed: '))
    apr = float(input('Enter your APR (Annual Percentage Rate): '))
    years = int(input('Enter the amount of years for the loan: '))
except ValueError:
    print('Incorrect input! You must enter numbers!')
else:
    print()
    loan = money_borrowed
    for year in range(years):
        loan *= (100 + apr) / 100
        print(f'Year {year + 1} is {locale.currency(loan, grouping=True)}')
    interest = loan - money_borrowed
    print()
    print(f'You paid {locale.currency(interest, grouping=True)} in interest!')
