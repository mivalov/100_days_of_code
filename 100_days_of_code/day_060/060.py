# Day 60: The Magic of Time

import datetime


def main() -> None:
    msg = '🌟Event Countdown Timer🌟\n'
    print(msg)
    event_name = input('Input the event: ')
    try:
        year = int(input('Input the year: '))
        month = int(input('Input the month: '))
        day = int(input('Input the day: '))
        event_date = datetime.date(year, month, day)
    except ValueError:
        print('Incorrect input!')
    else:
        today = datetime.date.today()
        diff = event_date - today
        diff = diff.days

        if diff > 0:
            print(f'{event_name} is in {diff} days.')
        elif diff < 0:
            print(f'You missed {event_name} by {abs(diff)} days.')
        else:
            print(f'🎉🎉 {event_name} is today! 🎉🎉')


if __name__ == '__main__':
    main()
