#N,M = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
#arr.sort(key=lambda x: (len(x),ord(x[0])))
#iDict = {value: index for index, value in enumerate(arr)}

from array import array
import collections
import sys
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

A1, A2 = map(int, sys.stdin.readline().split())
B1, B2 = map(int, sys.stdin.readline().split())

C2 = (A2*B2)// gcd(A2,B2)
C1 = (A1*(C2//A2)) + (B1*(C2//B2))

print(C1//gcd(C1,C2),C2//gcd(C1,C2))