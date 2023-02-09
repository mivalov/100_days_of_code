# Day 59: Palindrome

def is_palindrome(word: str) -> bool:
    """Check if a given string is palindrome using recursion."""
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])


# def is_palindrome(word: str) -> bool:
#     """Check if a given string is palindrome (alternative solution)."""
#     return word == word[::-1]


def main() -> None:
    msg = '🌟Palindrome Checker🌟\n'
    print(msg)
    # "racecar" is a palindrome
    word = input('Enter a word: ').strip().lower()
    if is_palindrome(word):
        print(f'{word.capitalize()} is a palindrome. Yay')
    else:
        print(f'{word.capitalize()} is not a palindrome. (;')


if __name__ == '__main__':
    main()
