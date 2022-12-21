# Day 9: Type casting

print('Generation Identifier')
print(21 * '=')

try:
    birth_year = int(input('Which year were you born? '))
except ValueError:
    print('You must enter digits! Try again..')
else:
    if birth_year >= 2012:
        print("You're part of Generation Alpha!")
    elif birth_year >= 1997:
        print("Okay, Zoomer!")
    elif birth_year >= 1982:
        print("Another Millennial on the horizon!")
    elif birth_year >= 1965:
        print("You're part of Generation X!")
    elif birth_year >= 1946:
        print("Okay, Boomer!")
    elif birth_year >= 1928:
        print("You're part of the Silent Generation!")
    elif birth_year >= 1901:
        print("You're part of the Greatest Generation!")
    elif birth_year >= 1982:
        print("You're part of the Lost Generation!")
    else:
        print("Generation unknown.. 😕")
