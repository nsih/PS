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
N = int(sys.stdin.readline())
list = list(map(int,sys.stdin.readline().split()))
answer = []
idx = 1
answer.append(idx)
for i in range(N-1):
    vec = list[idx-1]
    list[idx-1] = 0
    for _ in range(abs(vec)):
        if vec < 0:
            idx -= 1
            idx = (idx - 1) % N + 1
            while list[(idx - 1) % N] == 0:
                idx -= 1
                idx = (idx - 1) % N + 1
        elif vec > 0:
            idx += 1
            idx = (idx - 1) % N + 1
            while list[(idx-1) % N] == 0:
                idx += 1
                idx = (idx - 1) % N + 1
    answer.append(idx)
for item in answer:
    print(item,end=' ')