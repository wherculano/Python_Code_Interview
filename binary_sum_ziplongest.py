from itertools import zip_longest
from collections import deque


def minor_to_greater(str_bin):
    str_bin = map(int, reversed(str_bin))
    return str_bin


def binary_sum(n1: str, n2: str):
    """N1 and N2 are non negative binary numbers with arbitrary length"""
    n1 = minor_to_greater(n1)
    n2 = minor_to_greater(n2)
    result = deque()
    spare_digit = 0
    for d1, d2 in zip_longest(n1, n2, fillvalue=0):
        digits_sum = d1 + d2 + spare_digit
        spare_digit = 0 if digits_sum < 2 else 1
        result.appendleft(str(digits_sum % 2))
    if spare_digit == 1:
        result.appendleft('1')
    return ''.join(result)


print(binary_sum('111110', '1100'))  # 1001010
