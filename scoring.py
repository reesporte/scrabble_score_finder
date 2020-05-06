"""
Scoring functionality definitions

Tile quantity and point values obtained from https://en.wikipedia.org/wiki/Scrabble_letter_distributions.
"""
LETTERS = { #  name : [qty, pt val]
            'a' : [9, 1],
            'b' : [2, 3],
            'c' : [2, 3],
            'd' : [4, 2],
            'e' : [12, 1],
            'f' : [2, 4],
            'g' : [3, 2],
            'h' : [2, 4],
            'i' : [9, 1],
            'j' : [1, 8],
            'k' : [1, 5],
            'l' : [4, 1],
            'm' : [2, 3],
            'n' : [6, 1],
            'o' : [8, 1],
            'p' : [2, 3],
            'q' : [1, 10],
            'r' : [6, 1],
            's' : [4, 1],
            't' : [6, 1],
            'u' : [4, 1],
            'v' : [2, 4],
            'w' : [2, 4],
            'x' : [1, 8],
            'y' : [2, 4],
            'z' : [1, 10],
         }

WORDLIST = open("word_list.txt", "r+").read().split("\n")

def qty(letter):
    return LETTERS[letter][0]

def pts(letter):
    return LETTERS[letter][1]

def is_word_valid(word):
    """
    returns True if word is in word_list.txt
    """
    if word.upper() in WORDLIST:
        return True
    return False

def score(word):
    """
    On success:
        returns word score
    On error:
        if word uses a tile more times than allowed
        or
        word isn't in list
            returns 'Invalid word'
    """
    word = word.lower()
    invalid = 'Invalid word'

    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    alphabet.append('blank')
    uses = { tile : 0 for tile in alphabet }
    count = 0

    if not is_word_valid(word):
        return invalid

    for letter in word:
        if letter.isalpha() or letter == 'blank':
            uses[letter] += 1
            if uses[letter] <= qty(letter):
                count += pts(letter)
            else:
                return invalid
        else:
            # word contains non-alphabet characters
            return invalid

    return count

def debug():
    """
    used to check scoring functionality
    returns True if scoring works properly
    """

    result = True
    result &= (score("this") == 7)
    result &= (score("is") == 2)
    result &= (score("test") == 4)
    result &= (score("of") == 5)
    result &= (score("scoring") == 10)
    result &= (score("functionality") == 21)

    return result
