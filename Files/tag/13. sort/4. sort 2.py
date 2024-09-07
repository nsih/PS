#a,b = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
from array import array
import collections
import sys
N = int(sys.stdin.readline())

arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for item in arr:
    print(item)