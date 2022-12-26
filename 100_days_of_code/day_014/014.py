# Day 14: Rock, Paper, Scissors

from getpass import getpass


def game(player1_name: str, player1: str,
         player2_name: str, player2: str) -> None:
    if player1 == 'r':
        if player2 == 'r':
            print("You both picked Rock. It's a draw!")
        elif player2 == 's':
            print(f"{player1_name}'s Rock smashed {player2_name}'s Scissors!")
        elif player2 == 'p':
            print(f"{player1_name}'s Rock lost to {player2_name}'s Paper!")
        else:
            print(f'Invalid Move {player2_name}!')
    elif player1 == 'p':
        if player2 == 'r':
            print(f"{player2_name}'s Rock lost to {player1_name}'s Paper!")
        elif player2 == 's':
            print(f"{player1_name}'s Paper is cut into "
                  f"tiny pieces by {player2_name}'s Scissors!")
        elif player2 == 'p':
            print("You both picked Paper. It's a draw!")
        else:
            print(f'Invalid Move {player2_name}!')
    elif player1 == 's':
        if player2 == 'r':
            print(
                f"{player2_name}'s Rock wins over {player1_name}'s Scissors!")
        elif player2 == 's':
            print("You both picked Scissors. It's a draw!")
        elif player2 == 'p':
            print(f"{player2_name}'s Paper is cut into "
                  f"tiny pieces by {player1_name}'s Scissors!")
        else:
            print(f'Invalid Move {player2_name}!')
    else:
        print(f'Invalid Move {player1_name}!')


def main() -> None:
    print('EPIC 🪨 📄 ✂️  BATTLE', end='\n\n')
    print('Select your move (r, p or s)', end='\n\n')

    valid_moves = ['r', 'p', 's']
    player1_name = input('Player1 name: ')
    player2_name = input('Player2 name: ')
    player1, player2 = '', ''
    p1_valid, p2_valid = False, False
    while True:
        if not p1_valid:
            player1 = getpass(f"{player1_name}'s move: ").lower()
            if player1 in valid_moves:
                p1_valid = True
            else:
                print(f'Invalid Move {player1_name}! Choose "R" for Rock, '
                      '"P" for Paper or "S" for Scissors')
        elif not p2_valid:
            player2 = getpass(f"{player2_name}'s move: ").lower()
            if player2 in valid_moves:
                p2_valid = True
            else:
                print(f'Invalid Move {player2_name}! Choose "R" for Rock, '
                      '"P" for Paper or "S" for Scissors')
        else:
            break
    game(player1_name, player1, player2_name, player2)


if __name__ == '__main__':
    main()
