def binary_sum(n1: str, n2: str) -> str:
    """N1 and N2 are non negative binary numbers with arbitrary length"""
    n1 = int(n1, 2)
    n2 = int(n2, 2)
    return f'{n1+n2:0b}'
    # return format(n1+n2, 'b')


print(binary_sum('111110', '1100'))
