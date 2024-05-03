#sys.stdin.readline()

from array import array
import sys

N,M = map(int, sys.stdin.readline().split())

bucket = [0]*N

for _ in range(M):
    i,j,k = map(int, sys.stdin.readline().split())

    for idx in range(i-1,j):
        bucket[idx] = k

for item in bucket:
    print(item,end=' ')