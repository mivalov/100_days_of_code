# Day 54: CSV reader

import csv
from pathlib import Path


def main() -> None:
    file = Path('Day54Totals.csv')
    total = 0.0
    with open(file, 'r') as f_in:
        reader = csv.DictReader(f_in)
        for row in reader:
            total += float(row.get('Quantity', 0)) * float(row.get('Cost', 0))

    print(f'Total: ${round(total, 2)}')


if __name__ == '__main__':
    main()
