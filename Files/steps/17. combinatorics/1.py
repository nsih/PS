#N,M = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
#arr.sort(key=lambda x: (len(x),ord(x[0])))
#iDict = {value: index for index, value in enumerate(arr)}
#prime number
'''
#최대공약수
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
#소수판별 n**0.5
def isP(N):
    if N == 1:
        return False
    for i in range(2, int(N**0.5)+1):
        if N%i == 0:
            return False
    return True
    
#에라토스테네스의 체
prime = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1
'''
#
"""
.
"""
import select
from array import array
import collections
import math
from functools import reduce
import math
from functools import reduce
from collections import deque
import sys

n = int(sys.stdin.readline())

print(n*(n-1))