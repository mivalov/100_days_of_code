# Day 26: Music player

import os
import time

from replit import audio


def play():
    source = audio.play_file('audio.wav')
    source.paused = False  # unpause the playback
    while True:
        # Start taking user input and doing something with it
        stop = int(input(
            'Press 2 anytime to stop the song and go back to the menu: '))
        if stop == 2:
            source.paused = True
            return
        else:
            continue


def main() -> None:
    while True:
        # clear the screen
        os.system('clear')

        # Show the menu
        print('🎵 MyPOD Music Player')
        time.sleep(1)
        print('Press 1 to Play')
        print('Press 2 to Exit')
        time.sleep(1)
        print('Press anything else to see the menu again')

        # take user's input
        user_input = int(input())

        # check whether you should call the play() depending on user's input
        if user_input == 1:
            print('Playing some proper tunes!')
            play()
        elif user_input == 2:
            exit()
        else:
            continue


if __name__ == '__main__':
    main()
