#N,M = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
#arr.sort(key=lambda x: (len(x),ord(x[0])))
#iDict = {value: index for index, value in enumerate(arr)}

from array import array
import collections
import sys
S = sys.stdin.readline().strip()
sDic = {}
for i in range(1,len(S)+1):
    for j in range(0,len(S)+1-i):
        if S[j:j+i] not in sDic:
            sDic[S[j:j+i]] = 0
print(len(sDic))