#sys.stdin.readline()

from array import array
import sys

N,M = map(int,sys.stdin.readline().split())

buckets = []

for idx in range(N):
    buckets.append(idx+1)

for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())

    i-=1
    j-=1

    buckets[i:j+1] = reversed(buckets[i:j+1])

for ball in buckets:
    print(ball, end=' ')