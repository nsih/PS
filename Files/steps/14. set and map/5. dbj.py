#N,M = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
#arr.sort(key=lambda x: (len(x),ord(x[0])))
#iDict = {value: index for index, value in enumerate(arr)}

from array import array
import collections
import sys
N,M = map(int,sys.stdin.readline().split())

dbDic = {}

for _ in range(N+M):
    name = sys.stdin.readline().strip()
    if name not in dbDic:
        dbDic[name] = 0
    else:
        dbDic[name] += 1

sList = []
for item in dbDic:
    if dbDic[item] > 0:
        sList.append(item)

print(len(sList))
for item in sorted(sList):
    print(item)