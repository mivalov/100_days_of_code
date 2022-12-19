# Day 7: Nested if statements

print('Fake Fan Finder')
print(15 * '=')

anime = input("What's your favourite Anime? ").lower()
if anime == 'one piece':
    main_char = input(
        'Oh really?! Can you name me any of the main characters? '
    ).lower()
    if main_char == 'nami':
        role = input(
            'You got that by pure chance. '
            'Okay then, what is her job on the ship? '
        ).lower()
        if role == 'navigator':
            bounty = input('And what is her first bounty then? ').lower()
            if bounty == 'b 16 million':
                print('Correct!')
            else:
                print('See! Fake One piece fan!')
        else:
            print('See! Fake One piece fan!')
    elif main_char == 'luffy':
        role = input(
            'You got that by pure chance. '
            'Okay then, what is his job on the ship? '
        ).lower()
        if role == 'captain':
            bounty = input('And what is his first bounty then? ').lower()
            if bounty == 'b 30 million':
                print('Correct!')
            else:
                print('See! Fake One piece fan!')
    elif main_char == 'zoro':
        role = input(
            'You got that by pure chance. '
            'Okay then, what is his job on the ship? '
        ).lower()
        if role in ['first mate', 'combatant', 'swordsman']:
            bounty = input('And what is his first bounty then? ').lower()
            if bounty == 'b 60 million':
                print('Correct!')
            else:
                print('See! Fake One piece fan!')
    elif main_char == 'sanji':
        role = input(
            'You got that by pure chance. '
            'Okay then, what is his job on the ship? '
        ).lower()
        if role in ['chef', 'cook', 'combatant']:
            bounty = input('And what is his first bounty then? ').lower()
            if bounty == 'b 77 million':
                print('Correct!')
            else:
                print('See! Fake One piece fan!')
    elif main_char == 'chopper':
        role = input(
            'You got that by pure chance. '
            'Okay then, what is his job on the ship? '
        ).lower()
        if role == 'doctor':
            devil_fruit = input('What is his devil fruit called? ').lower()
            if devil_fruit in ['hito hito no mi', 'human-human fruit']:
                print('Correct!')
            else:
                print('See! Fake One piece fan!')
    elif main_char == 'robin':
        role = input(
            'You got that by pure chance. '
            'Okay then, what is her job on the ship? '
        ).lower()
        if role == 'archaeologist':
            bounty = input('And what is her first bounty then? ').lower()
            if bounty == 'b 79 million':
                print('Correct!')
            else:
                print('See! Fake One piece fan!')
        else:
            print('See! Fake One piece fan!')
    elif main_char == 'usopp':
        role = input(
            'You got that by pure chance. '
            'Okay then, what is his job on the ship? '
        ).lower()
        if role == 'sniper':
            bounty = input('And what is his first bounty then? ').lower()
            if bounty == 'b 30 million':
                print('Correct!')
        else:
            print('See! Fake One piece fan!')
    elif main_char == 'brook':
        role = input(
            'You got that by pure chance. '
            'Okay then, what is his job on the ship? '
        ).lower()
        if role == 'musician':
            bounty = input('And what is his first bounty then? ').lower()
            if bounty == 'b 33 million':
                print('Correct!')
            else:
                print('See! Fake One piece fan!')
    elif main_char == 'franky':
        role = input(
            'You got that by pure chance. '
            'Okay then, what is his job on the ship? '
        ).lower()
        if role == 'shipwright':
            bounty = input('And what is his first bounty then? ').lower()
            if bounty == 'b 44 million':
                print('Correct!')
            else:
                print('See! Fake One piece fan!')
    elif main_char == 'jinbe':
        role = input(
            'You got that by pure chance. '
            'Okay then, what is his job on the ship? '
        ).lower()
        if role == 'helmsman':
            bounty = input('And what is his bounty before '
                           'becoming a Warlord then? ').lower()
            if bounty == 'b 250 million':
                print('Correct!')
            else:
                print('See! Fake One piece fan!')
    else:
        print('See! Fake One piece fan!')
elif anime == 'tokyo ghoul':
    main_char = input(
        'Oh really?! Can you name me any of the main characters? '
    ).lower()
    if main_char == 'kaneki':
        alias = input('Pure luck! What is his most famous alias? ').lower()
        if alias == 'eyepatch':
            best_friend = input('And who is his best friend? ').lower()
            if best_friend in ['hide', 'nagichika', 'hideyoshi nagichika']:
                print('Correct!')
            else:
                print('See! Fake Tokyo Ghoul fan!')
        else:
            print('See! Fake Tokyo Ghoul fan!')
    elif main_char == 'touka':
        alias = input('Pure luck! What is her most famous alias? ').lower()
        if alias == 'rabbit':
            brother = input("What is her brother's name? ").lower()
            if brother == 'ayato':
                print('Correct!')
            else:
                print('See! Fake Tokyo Ghoul fan!')
        else:
            print('See! Fake Tokyo Ghoul fan!')
    else:
        print('See! Fake Tokyo Ghoul fan!')
else:
    print('Good for you!')
