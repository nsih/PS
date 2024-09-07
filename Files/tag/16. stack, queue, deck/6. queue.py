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
import sys

T = int(sys.stdin.readline())
queue = []
cnt = 0

for i in range(T):
    inputValue = sys.stdin.readline().strip()
    inputValues = inputValue.split()

    A = ''
    B = 0

    if len(inputValues) <= 1:
        A = inputValues[0]
    else:
        A = inputValues[0]
        B = int(inputValues[1])

    if A == 'push':
        queue.append(B)

    elif A == 'pop':
        if len(queue)-cnt:
            print(queue[0+cnt])
            cnt += 1
        else:
            print(-1)

    elif A == 'size':
        print(len(queue)-cnt)

    elif A == 'empty':
        if len(queue)-cnt:
            print(0)
        else :
            print(1)

    elif A == 'front':
        if len(queue)-cnt:
            print(queue[0+cnt])
        else :
            print(-1)

    elif A == 'back':
        if len(queue)-cnt:
            print(queue[-1])
        else :
            print(-1)

    #print(queue)