# Day 14: Epic Battle of Rock, Paper, Scissors (Part2)

from getpass import getpass
from typing import Tuple


def game(player1_name: str, p1_move: str, p1_score: int,
         player2_name: str, p2_move: str, p2_score: int) -> Tuple[int, int]:
    if p1_move == 'r':
        if p2_move == 'r':
            print("You both picked Rock. It's a draw!")
        elif p2_move == 's':
            p1_score += 1
            print(f"{player1_name}'s Rock smashed {player2_name}'s Scissors!")
        elif p2_move == 'p':
            p2_score += 1
            print(f"{player1_name}'s Rock lost to {player2_name}'s Paper!")
        else:
            print(f'Invalid Move {player2_name}!')
    elif p1_move == 'p':
        if p2_move == 'r':
            p1_score += 1
            print(f"{player2_name}'s Rock lost to {player1_name}'s Paper!")
        elif p2_move == 's':
            p2_score += 1
            print(f"{player1_name}'s Paper is cut into "
                  f"tiny pieces by {player2_name}'s Scissors!")
        elif p2_move == 'p':
            print("You both picked Paper. It's a draw!")
        else:
            print(f'Invalid Move {player2_name}!')
    elif p1_move == 's':
        if p2_move == 'r':
            p2_score += 1
            print(
                f"{player2_name}'s Rock wins over {player1_name}'s Scissors!")
        elif p2_move == 's':
            print("You both picked Scissors. It's a draw!")
        elif p2_move == 'p':
            p1_score += 1
            print(f"{player2_name}'s Paper is cut into "
                  f"tiny pieces by {player1_name}'s Scissors!")
        else:
            print(f'Invalid Move {player2_name}!')
    else:
        print(f'Invalid Move {player1_name}!')
    return p1_score, p2_score


def main() -> None:
    print('EPIC 🪨 📄 ✂️  BATTLE')
    #    print('EPIC \U0001FAA8 \U0001F4C4 \U00002702 BATTLE')
    print(20 * '=')
    print('Enter your names')
    print()
    valid_moves = ['r', 'p', 's']
    player1_name = input('Player1 name: ')
    player2_name = input('Player2 name: ')
    print(20 * '=')
    try:
        max_wins = int(input(
            'How many games should be won until a winner is recognised? '))
    except ValueError:
        print('Incorrect input! Defaults to 3.')
        max_wins = 3
    print('Select your move (r, p or s)', end='\n\n')
    p1_move, p2_move = '', ''
    p1_valid, p2_valid = False, False
    p1_score, p2_score = 0, 0
    total_games = 0
    while True:
        if not p1_valid:
            p1_move = getpass(f"{player1_name}'s move: ").lower()
            if p1_move in valid_moves:
                p1_valid = True
            else:
                print(f'Invalid Move {player1_name}! Choose "R" for Rock, '
                      '"P" for Paper or "S" for Scissors')
        elif not p2_valid:
            p2_move = getpass(f"{player2_name}'s move: ").lower()
            if p2_move in valid_moves:
                p2_valid = True
            else:
                print(f'Invalid Move {player2_name}! Choose "R" for Rock, '
                      '"P" for Paper or "S" for Scissors')
        else:
            total_games += 1
            print()
            print(f'Results of game {total_games}:')
            p1_score, p2_score = game(player1_name, p1_move, p1_score,
                                      player2_name, p2_move, p2_score)
            p1_valid, p2_valid = False, False
            print(
                '',
                'Score:',
                f'\t{player1_name}: {p1_score}',
                f'\t{player2_name}: {p2_score}',
                20 * '=',
                sep='\n'
            )
            if p1_score == max_wins:
                print(f'After a total of {total_games} games, {player1_name} '
                      f'wins the battle! Congratulations!')
                break
            elif p2_score == max_wins:
                print(f'After a total of {total_games} games, {player2_name} '
                      f'wins the battle! Congratulations!')
                break


if __name__ == '__main__':
    main()
