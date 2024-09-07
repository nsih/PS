#N,M = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
#arr.sort(key=lambda x: (len(x),ord(x[0])))
#iDict = {value: index for index, value in enumerate(arr)}

from array import array
import collections
import sys
N = int(sys.stdin.readline())
dic = {}
cList = list(map(int, sys.stdin.readline().split()))

for i in cList:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

M = int(sys.stdin.readline())
countList = list(map(int, sys.stdin.readline().split()))

for idx in range(M):
    if countList[idx] in dic :
        print(dic[countList[idx]],end=' ')
    else :
        print(0,end=' ')