""" 
Reverse Words in a String
Given a string s, reverse the order of the words. Words are separated by spaces.
The output string should contain the words in reverse order with a single space between them.

>>> reverse_1("the sky is blue")
'blue is sky the'

>>> reverse_1("hello world")
'world hello'

>>> reverse_1("python coding interview")
'interview coding python'

>>> reverse_2("the sky is blue")
'blue is sky the'

>>> reverse_2("hello world")
'world hello'

>>> reverse_2("python coding interview")
'interview coding python'
"""


def reverse_1(string: str) -> str:  # O(n²) no pior caso ja que cria sempre um novo objeto
    new_string = ""
    for s in string.split()[::-1]:
        new_string += s + " "
    return new_string.strip()


def reverse_2(string: str) -> str:
    return " ".join(string.split()[::-1])  # O(n), cria uma lista


def reverse_3(string: str) -> str:
    return " ".join(reversed(string.split()))  # O(n) cria um iterador, usa menos memoria. Melhor opcao!


if __name__ == "__main__":
    from doctest import testmod
    testmod()
