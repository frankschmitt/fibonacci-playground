import sys

def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


N = int(sys.argv[1])
print(fib(N))
