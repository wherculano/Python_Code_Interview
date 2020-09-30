"""
Given a text, try to find the number of holes in it
>>> number_of_holes('Boat')
4
>>> number_of_holes('Python Code Interview')
7
>>> number_of_holes('Python is the Best language ever')
13
"""


def number_of_holes(string):
    letters_with_holes = {'q': 1, 'Q': 1, 'e': 1, 'R': 1, 'o': 1, '1': 0, 'p': 1, 'P': 1,
                          'a': 1, 'A': 1, 'd': 1, 'D': 1, 'g': 1, 'b': 1, 'B': 2}

    number = 0
    for letter in string:
        if letter in letters_with_holes:
            number += letters_with_holes[letter]
    return number
