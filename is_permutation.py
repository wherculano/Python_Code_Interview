"""
Given two strings, write a method to decide if one is a permutation of the other.
"""


def is_perm_1(str_1: str, str_2: str) -> bool:
    str_1 = ''.join(sorted(str_1.lower()))
    str_2 = ''.join(sorted(str_2.lower()))
    if str_1 == str_2:
        return True
    return False


def is_perm_2(str_1: str, str_2: str) -> bool:
    str_1 = ''.join(sorted(str_1.lower()))
    str_2 = ''.join(sorted(str_2.lower()))
    if len(str_1) != len(str_2):
        return False
    for i in range(len(str_1)):
        if str_1[i] != str_2[i]:
            return False
    return True


def is_perm_3(str_1: str, str_2: str) -> bool:
    str_1 = ''.join(sorted(str_1.lower()))
    str_2 = ''.join(sorted(str_2.lower()))

    if len(str_1) != len(str_2):
        return False

    d = dict()

    for char in str_1:
        if char in d:
            d[char] -= 1
        else:
            d[char] = 1

    for char in str_2:
        if char in d:
            d[char] -= 1
        else:
            d[char] = 1

    return all(values == 0 for values in d.values())


is_permutation_1 = 'God'
is_permutation_2 = 'dog'

not_permutation_1 = 'not'
not_permutation_2 = 'Top'

print(' is_perm_1 '.center(20, '='))
print(is_perm_1(is_permutation_1, is_permutation_2))
print(is_perm_1(not_permutation_1, not_permutation_2))

print(' is_perm_2 '.center(20, '='))
print(is_perm_2(is_permutation_1, is_permutation_2))
print(is_perm_2(not_permutation_1, not_permutation_2))

print(' is_perm_3 '.center(20, '='))
print(is_perm_3(is_permutation_1, is_permutation_2))
print(is_perm_3(not_permutation_1, not_permutation_2))
