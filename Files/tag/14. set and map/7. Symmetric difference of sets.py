#N,M = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
#arr.sort(key=lambda x: (len(x),ord(x[0])))
#iDict = {value: index for index, value in enumerate(arr)}

from array import array
import collections
import sys
N,M = map(int,sys.stdin.readline().split())
nDic = {i:0 for i in list(map(int,sys.stdin.readline().split()))}
mDic = {i:0 for i in list(map(int,sys.stdin.readline().split()))}
count = 0
for key in nDic:
    if key not in mDic:
        count += 1
for key in mDic:
    if key not in nDic:
        count += 1
print(count)