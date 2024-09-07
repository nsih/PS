import sys

def fib1(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)
N = int(sys.stdin.readline())
print(fib1(N),N-2)