# Day 39: Hangman
import os
import platform
import random
import time

WORDS = (
    'ant baboon badger bat bear beaver camel cat clam cobra cougar '
    'coyote crow deer dog donkey duck eagle ferret fox frog goat '
    'goose hawk lion lizard llama mole monkey moose mouse mule newt '
    'otter owl panda parrot pigeon python rabbit ram rat raven rhino '
    'salmon seal shark sheep skunk sloth snake spider stork swan '
    'tiger toad trout turkey turtle weasel whale wolf wombat zebra'
).split()

HANGMAN_PICS = [r'''
   +-----+
   |     |
   |     O
   |    /|\
   |    / \
   |
==============
''', r'''
   +-----+
   |     |
   |     O
   |    /|\
   |    /
   |
==============
''', r'''
   +-----+
   |     |
   |     O
   |    /|\
   |
   |
==============
''', r'''
   +-----+
   |     |
   |     O
   |     |\
   |
   |
==============
''', r'''
   +-----+
   |     |
   |     O
   |     |
   |
   |
==============
''', r'''
   +-----+
   |     |
   |     O
   |
   |
   |
==============
''', r'''
   +-----+
   |     |
   |
   |
   |
   |
==============
''']


def corss_platform_clear() -> str:
    """Checks local system and returns its clear screen command."""
    local_system = platform.system().lower()
    if local_system in ['linux', 'darwin']:
        return 'clear'
    elif local_system == 'windows':
        return 'cls'
    else:
        raise SystemExit


def main() -> None:
    clear_command = corss_platform_clear()
    msg = '🌟 Hangman 🌟  '
    underline = 20 * '='
    lives = 6
    word = random.choice(WORDS)
    picked_letters = set()
    shown_word = len(word) * '_'
    while True:
        os.system(f'{clear_command}')
        print(f'{msg: ^20}', underline, sep='\n')
        print('', f'{shown_word: ^20}', '', sep='\n')
        if lives <= 0:
            print(HANGMAN_PICS[0])
            print(f'Game Over! The word was {word}')
            break
        else:
            print(f'Lives: {lives * "♥ "}')
        print(HANGMAN_PICS[lives])
        if shown_word == word:
            print(f'You won with {lives} lives left!')
            break
        letter = input('Choose a letter: ').strip().lower()
        if letter in picked_letters:
            print('You have already tried this letter before')
        elif len(letter) != 1:
            print('You must pick a letter!')
        elif not letter.isalpha():
            print('You must pick a letter!')
        else:
            picked_letters.add(letter)
            if letter in word:
                print('Correct!')
            else:
                print(f'Nope! There is no "{letter}" in this word.')
                lives -= 1
            shown_word = ''
            for char in word:
                if char in picked_letters:
                    shown_word += char
                else:
                    shown_word += '_'

        time.sleep(2)


if __name__ == '__main__':
    main()
