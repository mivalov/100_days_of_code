# Day 15: While Loop

def animal_sounds(animal: str = 'cow') -> str:
    """Returns the sound/text of a given animal."""
    if animal == 'cow':
        sound = 'moo'
    elif animal == 'cat':
        sound = 'meow'
    elif animal == 'dog':
        sound = 'woof'
    elif animal == 'lion':
        sound = 'roar'
    elif animal == 'horse':
        sound = 'neigh'
    elif animal in ['goat', 'sheep']:
        sound = 'baa'
    elif animal == 'pig':
        sound = 'oink'
    elif animal == 'donkey':
        sound = 'hee-haw'
    elif animal == 'chicken':
        sound = 'cluck'
    elif animal == 'rooster':
        sound = 'cock-a-doodle-do'
    elif animal == 'bird':
        sound = 'chirp'
    elif animal == 'owl':
        sound = 'hoot'
    elif animal == 'duck':
        sound = 'quack'
    elif animal == 'goose':
        sound = 'honk'
    elif animal == 'turkey':
        sound = 'gobble'
    elif animal == 'mosquito':
        sound = 'buzz'
    elif animal == 'cricket':
        sound = 'chirp'
    elif animal == 'frog':
        sound = 'ribbit'
    else:
        return "I don't know how this animal sounds like.. :("
    return f'The {animal} goes {sound}.'


def main() -> None:
    keep_playing = ''
    while keep_playing in ['', 'yes', 'y', 'yeah']:
        animal = input('What animal do you want? ').lower()
        print(animal_sounds(animal))
        keep_playing = input('Do you want to keep playing? [Y]es/No: ').lower()


if __name__ == '__main__':
    main()
