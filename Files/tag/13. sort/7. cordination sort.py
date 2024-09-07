#a,b = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
from array import array
import collections
import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append( list(map(int,sys.stdin.readline().split()) ))
arr.sort()
for i in range(len(arr)):
    print(arr[i][0],arr[i][1])