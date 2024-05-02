#sys.stdin.readline()

from array import array
import sys

N,M = map(int, sys.stdin.readline().split())

bucket = []

for i in range(N):
    bucket.append(i+1)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    bucket[i-1],bucket[j-1] = bucket[j-1],bucket[i-1]

for ball in bucket:
    print(ball,end=' ')