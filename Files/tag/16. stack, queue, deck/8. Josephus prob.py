#N,M = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
#arr.sort(key=lambda x: (len(x),ord(x[0])))
#iDict = {value: index for index, value in enumerate(arr)}
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
            
#스택 클래스
class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            #print(self.stack[-1])
            return self.stack.pop()
        else:
            print("-1")

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("-1")

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)
'''
import select
from array import array
import collections
import math
from functools import reduce
import math
from functools import reduce
from collections import deque
import sys

N,K = map(int,sys.stdin.readline().split())
list = [i for i in range(1, N + 1)]
answer = []
head = 0

for _ in range(N):
    head = (head + K - 1) % len(list)
    answer.append(list[head])
    list.pop(head)

print("<",end='')
for idx in range(len(answer)):
    if idx != len(answer)-1:
        print(answer[idx],end=', ')
    else:
        print(answer[idx], end='')
print(">",end='')