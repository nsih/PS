#a,b = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
from array import array
import collections
import sys

N = int(sys.stdin.readline())

n = 0
for n in range (0,6):
    if N // 10**(n+1) == 0:
        break
    else:
        n += 1

start = N-(9*(n+1))
if start<0:
    start = 0

min = N
for i in range(start,N):
    sum = i
    for j in range(0,n+1):
        sum += ( i // (10**j) ) % 10
    if sum == N:
        min = i
        break

if min == N:
    print(0)
else:
    print(min)