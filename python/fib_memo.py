import sys

def fib(n, memo={}):
    if not n in memo:
        if n == 0:
            res= 1
        elif n == 1:
            res= 1
        else: 
            res = fib(n-1, memo) + fib(n-2, memo)
        memo[n] = res
    return memo[n]

N = int(sys.argv[1])
memo = {}
print(fib(N, memo))
