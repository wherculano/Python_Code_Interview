def fib(n):
    a, b = 0, 1
    for i in range(n + 1):
        print(f'{a}', end=' -> ')
        a, b = b, a + b
    print('END')


fib(7)
