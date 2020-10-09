"""
Given an input string, reverse the string word by word.
A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and
the words are always separated by a single space.

Could you do it in-place without allocating extra space?
https://www.programcreek.com/2014/05/leetcode-reverse-words-in-a-string-ii-java/
"""
from collections import deque

from typing import Iterable


# First solution
def reverter_palavras(frase: str) -> str:
    """
    >>> reverter_palavras('the sky is blue')
    'blue is sky the'

    """
    palavras_separadas = frase.split()
    palavras_separadas.reverse()  # mais claro e mais explicito

    return ' '.join(palavras_separadas)


# Second solution
def reserved_words_constant_time_with_constant_length(frase: str) -> Iterable:
    """
    >>> list(reserved_words_constant_time_with_constant_length('the sky is blue'))
    ['blue', 'is', 'sky', 'the']

    """
    palavra = deque()

    for letra in reversed(frase):
        if letra == ' ':
            yield ''.join(palavra)
            palavra.clear()
        else:
            palavra.appendleft(letra)
    yield ''.join(palavra)
