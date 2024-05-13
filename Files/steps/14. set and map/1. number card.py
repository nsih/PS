#a,b = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
#arr.sort(key=lambda x: (len(x),ord(x[0])))
#iDict = {value: index for index, value in enumerate(arr)}

from array import array
import collections
import sys
N = int(sys.stdin.readline())
set = set( map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr = list( map(int,sys.stdin.readline().split()))
for i in arr:
    if i in set:
        print(1,end=' ')
    else:
        print(0,end=' ')