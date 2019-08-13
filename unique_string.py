"""
Implement an algorithm to determine if a string has all unique characters
"""

unique_str = 'aBcDeFG'
non_unique_str = 'Banana is good'


def normalize(input_str: str) -> str:
    """return a normalized string without spaces nor capital letters"""
    input_str = input_str.replace(" ", "")
    return input_str.lower()


def is_unique_1(input_str: str) -> bool:
    """
    store each letter in a dictionary. If the letter already exists in the dictionary returns false
    :return: bool
    """
    d = dict()
    for char in input_str:
        if char in d:
            return False
        d[char] = 1
    return True


def is_unique_2(input_str: str) -> bool:
    """Comparing if the length of the string is equal to the length of set characters"""
    return len(input_str) == len(set(input_str))


unique_str = normalize(unique_str)
non_unique_str = normalize(non_unique_str)

print(' is_unique_1 '.center(20, '#'))
print(is_unique_1(unique_str))
print(is_unique_1(non_unique_str))

print()

print(' is_unique_2 '.center(20, '#'))
print(is_unique_2(unique_str))
print(is_unique_2(non_unique_str))
