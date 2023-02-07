# Day 57: Recursion - Factorial finder


def factorial(number: int) -> int:
    """Calculate the factorial of a given number and return the result."""
    if number < 0:
        print('Factorial does not exist for negative numbers.')
    elif number == 0 or number == 1:
        return 1  # saves an unnecessary iteration
    else:
        return number * factorial(number - 1)


def main() -> None:
    msg = '🌟Factorial Finder🌟 \n'
    print(msg)
    try:
        number = int(input('Enter a number: '))
    except ValueError:
        print('Incorrect input! You must enter a positive whole number.')
    else:
        print(f'{number}! = {factorial(number)}')


if __name__ == '__main__':
    main()
