#N,M = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
#arr.sort(key=lambda x: (len(x),ord(x[0])))
#iDict = {value: index for index, value in enumerate(arr)}
'''
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
'''

from array import array
import collections
import math
from functools import reduce
import math
from functools import reduce
import sys

def isP(N):
    p = True
    for i in range(2, int(N**0.5)+1):
        if N%i == 0:
            p = False
            break
    return p

def nextP(N):
    if N == 0 or N==1:
        return 2
    else:
        while True:
            if isP(N):
                break
            else :
                N += 1
        return N

N = int(sys.stdin.readline())

for i in range(N):
    print(nextP(int(sys.stdin.readline())))