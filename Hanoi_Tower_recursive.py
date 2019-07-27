def hanoi(n, orig='A', aux='B', dest='C'):
    """
    Recursive solution to Tower of Hanoi
    :param n: number of disks
    :param orig: source
    :param aux: spare peg
    :param dest: target peg
    :return: String
    """
    if n >= 1:
        hanoi(n-1, orig, dest, aux)
        print(f'put {n} from {orig} to {dest} ')
        hanoi(n-1, aux, orig, dest)


if __name__ == '__main__':
    for value in range(1, 4):
        print(f' HANOI: {value} '.center(20, '#'))
        hanoi(value)
