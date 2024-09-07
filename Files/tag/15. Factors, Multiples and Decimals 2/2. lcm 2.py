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

A, B = map(int, sys.stdin.readline().split())
print((A*B)//gcd(A,B))

#https://www.acmicpc.net/status?from_mine=1&problem_id=13241&user_id=sih6571