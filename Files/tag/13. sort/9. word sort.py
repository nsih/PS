#a,b = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
#arr.sort(key=lambda x: (len(x),ord(x[0])))
from array import array
import collections
import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append( sys.stdin.readline().strip() )

arr = list(set(arr))
arr.sort(key=lambda x: (len(x),x))

for i in arr:
    print(i)