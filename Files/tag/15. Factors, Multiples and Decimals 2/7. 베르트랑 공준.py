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
'''
def isP(N):
    p = True
    if N == 1:
        return False
    for i in range(2, int(N**0.5)+1):
        if N%i == 0:
            p = False
            break
    return p
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
    if N == 1:
        return False
    for i in range(2, int(N**0.5)+1):
        if N%i == 0:
            p = False
            break
    return p

arr = []
for i in range(1,(123456*2)+1):
    if isP(i):
        arr.append(i)
    else:
        arr.append(0)

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break;
    count = 0
    for i in range(N+1,(N*2)+1):
        if arr[i-1] > 0:
            count+=1
    print(count)