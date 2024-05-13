#a,b = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
#arr.sort(key=lambda x: (len(x),ord(x[0])))
#iDict = {value: index for index, value in enumerate(arr)}

from array import array
import collections
import sys

N = int(sys.stdin.readline())
arr = list( map(int,sys.stdin.readline().split()))

iDict = {value: index for index, value in enumerate(sorted(set(arr)))}

for i in range(len(arr)):
    print(iDict[arr[i]], end=' ')