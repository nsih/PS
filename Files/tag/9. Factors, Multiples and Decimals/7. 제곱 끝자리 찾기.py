def findA(n):
    for x in range(n-1, 0, -1):
        k = len(str(x))

        if isA(x, k) == 1:
            return x
    return -1

def isA(x, k):
    xS = x ** 2
    kM = 10 ** k

    if xS % kM == x:
        return 1
    else:
        return 0

import sys

n = int(sys.stdin.readline())

print(findA(n))