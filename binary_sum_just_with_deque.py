from collections import deque


def minor_to_greater(str_bin):
    # "manual" reversed and map
    result = []
    str_bin = list(str_bin)
    while str_bin:
        result.append(int(str_bin.pop()))
    return result


# "manual" zip_longest
def zip_longest(n1, n2, fillvalue):
    n1 = list(n1)
    n2 = list(n2)
    minor, greater = sorted([n1, n2], key=len)
    missing_zeros = len(greater) - len(minor)
    minor.extend([fillvalue] * missing_zeros)
    # "manual" zip
    result = []
    for index, digit in enumerate(greater):
        result.append((digit, minor[index]))
    return result


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
