# Day 4: 'Print' in Colour!

print(10 * '=', 'Welcome to your adventure simulator', 10 * '=')
print(
    'I am going to ask you a bunch of questions and '
    'then create an epic story with you as the star!'
)
print()

name = input('What is your name? ')
name = f'\033[35m{name}\033[0m'
enemy_name = input("What is your worst enemy's name? ")
enemy_name = f'\033[31m{enemy_name}\033[0m'
power = input('What is your superpower? ')
power = f'\033[34m{power}\033[0m'
place = input('Where do you live? ')
place = f'\033[33m{place}\033[0m'
fav_food = input('What is your favourite food? ')
fav_food = f'\033[32m{fav_food}\033[0m'

print()
print(
    f"Hello {name}! Your ability to {power} will make sure you never "
    f"have to look at {enemy_name} again. Go eat {fav_food} as you "
    f"walk down the streets of {place} and use {power} for good and not evil!"
)
