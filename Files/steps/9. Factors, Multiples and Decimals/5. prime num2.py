#a,b = map(int,sys.stdin.readline().split())

from array import array

import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

sum = 0
min = 0

for i in range(M,N+1):
    isP = True
    for j in range(2, i):
        if i % j == 0:
            isP = False
            break;

    if i == 1:
        isP = False

    if isP:
        if sum == 0:
            min = i
        sum += i


if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)