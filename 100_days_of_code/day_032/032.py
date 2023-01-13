# Day 32: Lists
from random import choice


def main() -> None:
    greetings = [
        'Hi',  # english
        'Salut',  # french
        'Zdrasti',  # bulgarian
        'Nǐ hǎo',  # chinese
        'Ciao',  # italian
        'Yā',  # japanese
        'Hallo',  # german
        'Oi',  # portuguese
        'Hei',  # norwegian
    ]
    print(choice(greetings))


if __name__ == '__main__':
    main()
