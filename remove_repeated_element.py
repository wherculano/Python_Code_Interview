def remove_duplicity(lst):
    result = list()
    repeated = set()
    for element in lst:
        if element not in repeated:  # set: constant time. list: linear time
            result.append(element)
            repeated.add(element)
    return result  # keep the same order or sorted(result) to order


print(remove_duplicity(['banana', 'caqui', 'abacaxi', 'banana', 'maçã']))
