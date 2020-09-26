"""
>>> check_anagram('biro')
biro bior brio broi boir bori 
ibro ibor irbo irob iobr iorb 
rbio rboi ribo riob robi roib 
obir obri oibr oirb orbi orib 
"""

from itertools import permutations


def check_anagram(string):
    """This function returns all possible anagrams of a given word"""
    comb = list(permutations(string, 4))
    for index, word in enumerate(comb, start=1):
        print(''.join(word), end=' ')
        if index % 6 == 0:
            print()
