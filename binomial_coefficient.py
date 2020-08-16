"""Calculation of binomial coefficient.
n! / k!(n-k)!

#  Doctest
>>> fatorial(5)
120
>>> fatorial(6)
120
>>> binomial_coefficient(10, 6)
210
"""

def fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        for i in range(2,n+1):
            fat *= i
    return fat

def binomial_coefficient(n, k):
    return fatorial(n) // (fatorial(k) * fatorial(n - k))

#  PyTest
def test_fat():
    assert fatorial(5) == 120
    assert fatorial(6) == 721