import random
import os
import time

trumps = dict()
trumps['Cap Morgan'] = {'Intelligence': 199, 'Handsomeness': 84,
                        'L33t c0ding skillz': 55, 'Baldness Level': 0}
trumps["Obi-Wan Kenobi"] = {"Intelligence": 200, "Handsomeness": 50,
                            "L33t c0ding skillz": 50, "Baldness Level": 0}
trumps["Joey (Friends)"] = {"Intelligence": 150, "Handsomeness": 50,
                            "L33t c0ding skillz": 1, "Baldness Level": 0}
trumps["Professor X"] = {"Intelligence": 300, "Handsomeness": 10,
                         "L33t c0ding skillz": 250, "Baldness Level": 100}

while True:
    print(
        '🌟 TOP TRUMPS 🌟', '',
        'Characters', '',
        sep='\n'
    )
    for key in trumps:
        print(key)
    user = input("\nPick your character: ")
    comp = random.choice(list(trumps.keys()))
    print(f'Computer has picked {comp}')

    print('Choose your stat: Intelligence, Handsomeness, '
          'L33t c0ding skillz & Baldness Level')

    answer = input('> ')

    print(f"{user}: {trumps[user][answer]}")
    print(f"{comp}: {trumps[comp][answer]}")

    if trumps[user][answer] > trumps[comp][answer]:
        print(user, 'wins')
    elif trumps[user][answer] < trumps[comp][answer]:
        print(comp, 'wins')
    else:
        print('Draw')

    time.sleep(2)
    os.system('clear')
