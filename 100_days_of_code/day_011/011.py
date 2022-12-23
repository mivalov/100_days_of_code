# Day 11: Amount of seconds in a year

def is_leap_year(year: int) -> bool:
    """Check if given year is a leap year or not

    A leap year is exactly divisible by 4, except for century years (xx00).
    The century year is a leap year only if it is perfectly divisible by 400.
    For example:
        2022 is not a leap year;
        2012 is a leap year;
        2000 is a leap year;
        1994 is not a leap year;
        1900 is not a leap year
    """
    if year % 400 == 0 and year % 100 == 0:
        return True  # century year is a leap year
    elif year % 4 == 0 and year % 100 != 0:
        return True  # non-century year, divisible by 4 is a leap year
    else:
        return False  # not a leap year


def main() -> None:
    try:
        year = int(input('Enter a year: '))
    except ValueError:
        print('Wrong input! Please enter a year.')
    else:
        seconds_in_minute = 60
        minutes_in_hour = 60
        hours_in_day = 24
        days_in_year = 366 if is_leap_year(year) else 365
        result = (
                days_in_year
                * hours_in_day
                * minutes_in_hour
                * seconds_in_minute
        )
        if days_in_year == 366:
            print(f'{year} is a leap year.')
        else:
            print(f'{year} is not a leap year.')
        print(f'The amount of seconds for the year {year} is {result:,}')


if __name__ == '__main__':
    main()
