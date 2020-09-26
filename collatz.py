"""
>>> collatz(1)
1 -> 4 -> 2 -> 1
>>> collatz(8)
8 -> 4 -> 2 -> 1
>>> collatz(13)
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

>>> total_collatz(13)
{13: 10}
>>> total_collatz(1)
{1: 4}
>>> total_collatz(8)
{8: 4}
"""


def collatz(num):
    """This function returns all elements from a number in Collatz sequence"""
    print(num, end=' -> ')
    while True:
        if num % 2 == 0:
            num //= 2
            print(num, end='')
        else:
            num = 3 * num + 1
            print(num, end='')
        if num == 1:
            break
        else:
            print(' -> ', end='')


def total_collatz(num):
    """This function returns the number and total of the numbers from Collatz sequence"""
    total = {}
    total_elements = [num]
    while True:
        if num % 2 == 0:
            num //= 2
            total_elements.append(num)
        else:
            num = 3 * num + 1
            total_elements.append(num)
        if num == 1:
            total[total_elements[0]] = len(total_elements)
            return total
            break
