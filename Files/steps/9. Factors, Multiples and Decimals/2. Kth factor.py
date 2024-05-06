#a,b = map(int,sys.stdin.readline().split())

from array import array

import sys

N,K = map(int,sys.stdin.readline().split())

count = 0;
for i in range(1,N+1):
    if N%i == 0:
        count += 1

    if count == K:
        print(i)
        break

if count < K:
    print("0")