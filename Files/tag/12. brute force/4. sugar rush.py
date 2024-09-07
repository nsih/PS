#a,b = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
from array import array
import collections
import sys
N = int(sys.stdin.readline())
arr = []
for i in range(0, N//5+1):
    for j in range(0, N//3+1):
        if N - (5 * i) - (3 * j) == 0:
            arr.append(i+j)

print(len(arr))
if len(arr) == 0:
    print(-1)
else:
    print(min(arr))