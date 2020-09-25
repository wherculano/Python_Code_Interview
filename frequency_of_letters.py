"""
>>> counter('banana')
{'b': 1, 'a': 3, 'n': 2}
>>> counter('parallelepiped')
{'p': 3, 'a': 2, 'r': 1, 'l': 3, 'e': 3, 'i': 1, 'd': 1}
"""


def counter(string: str) -> dict:
    """This function returns the frequency of each letter of a given word"""
    dct = {}
    for letter in string:
        dct[letter] = dct.get(letter, 0) + 1
    return dct
