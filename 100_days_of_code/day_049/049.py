# Day 49: Read from a file

def main() -> None:
    print('🌟Current Leader🌟')
    print('\nAnalyzing high scores...\n')
    file = 'high.score'
    highest_score = 0
    name = None
    with open(file, 'r') as stream:
        for line in stream:
            initials, score = line.strip().split()
            score = int(score)
            if score > highest_score:
                highest_score = score
                name = initials
    print(f'{name}: {highest_score}')


if __name__ == '__main__':
    main()
