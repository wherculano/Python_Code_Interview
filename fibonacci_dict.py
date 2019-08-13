def fib_rec(n):
    fib_dict = {0: 1, 1: 1}
    if fib_dict.__contains__(n):
        return fib_dict[n]
    new_fib_dict = fib_rec(n - 1) + fib_rec(n - 2)
    fib_dict[n] = new_fib_dict
    return new_fib_dict


for i in range(7):
    print(fib_rec(i), end=' -> ')
print('END')
