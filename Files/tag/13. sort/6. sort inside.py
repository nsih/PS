#a,b = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
from array import array
import collections
import sys
N = sys.stdin.readline().strip()
arr = []
for item in N:
    arr.append(int(item))
for item in sorted(arr,reverse=True):
    print(item,end='')