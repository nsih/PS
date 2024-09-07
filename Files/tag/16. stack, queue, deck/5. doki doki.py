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
input = list(map(int,sys.stdin.readline().split()))

start = input[:]
middle = []
end = []

#1을 end에 넣기위한 단계
for i in range(len(input)):
    if input[i] == 1:
        end.append(input[i])
        start.remove(input[i])
        break
    else:
        middle.append(input[i])
        start.remove(input[i])
#middle에서 end로 이동. 없으면 start에서 middle로 하나 데려와서 다시 검사
while len(start):
    if middle and end[-1] == middle[-1]-1:
        end.append(middle[-1])
        middle.pop()
    else:
        middle.append(start[0])
        start.pop(0)
#정리된 middle에서. end에 넣기위한 단계
while len(middle):
    if end[-1] == middle[-1]-1:
        end.append(middle[-1])
        middle.pop()
    else:
        print("Sad")
        break

if not len(middle) and not len(start):
    print("Nice")