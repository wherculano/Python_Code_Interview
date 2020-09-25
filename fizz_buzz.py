"""
>>> fizz_buzz(6)
1
fizz
buzz
fizz
5
fizzbuzz
>>> fizz_buzz(1)
1
>>> fizz_buzz(2)
1
fizz
"""


def fizz_buzz(num):
    for n in range(1, num + 1):
        if n % (2 * 3) == 0:
            print('fizzbuzz')
        elif n % 2 == 0:
            print('fizz')
        elif n % 3 == 0:
            print('buzz')
        else:
            print(n)
