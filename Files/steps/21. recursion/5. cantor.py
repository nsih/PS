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
#memoization
"""
#메모이제이션 팩토리얼
memo = {0: 1, 1: 1}
def facMem(n):
    if n in memo:   #캐싱된 것 중에 N이 있으면 바로 N번째 반환
        return memo[n]

    #아니면 N을 캐시메모리에서 리턴할 수 있을때 까지 캐싱된걸 활용해 dic에 추가
    memo[n] = n * facMem(n-1)
    return memo[n]
"""
import select
from array import array
import collections
import math
from functools import reduce
from collections import deque
import math
from collections import Counter
import sys

def cantor(lst,s,e):
    p1 = s + ((e-s+1)//3)
    p2 = s + (((e-s+1)//3)*2)

    if e-s >= 2:
        for i in range(p1, p2):
            lst[i] = ' '
        cantor(lst,s,p1-1)
        cantor(lst,p2,e)


for line in sys.stdin:
    line = line.strip()

    if line:
        N = int(line)

        lst = []
        for i in range(3**N):
            lst.append('-')

        cantor(lst,0,len(lst)-1)

        for item in lst:
            print(item,end='')
        print('')
    else:
        break