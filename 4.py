#fibonacci
import time
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

start = time.time()
print(fib(15))
print(time.time()-start)
print(fib(35))
print(time.time()-start)
print(fib(36))
print(time.time()-start)
print(fib(39))
print(time.time()-start)