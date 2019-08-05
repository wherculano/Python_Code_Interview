def fib_rec(n):
    if n == 0 or n == 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


for i in range(8):
    print(fib_rec(i), end=' -> ')
print('END')
