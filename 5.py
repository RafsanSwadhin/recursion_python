def fib(n,d):

    if n in d:
        return d[n]
    else:
        d[n] = fib(n-1,d) + fib(n-1,d)
        return d[n]

d = {0:1,1:1}
print(fib(15,d))