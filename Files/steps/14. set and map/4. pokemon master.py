#a,b = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
#arr.sort(key=lambda x: (len(x),ord(x[0])))
#iDict = {value: index for index, value in enumerate(arr)}

from array import array
import collections
import sys
N,M = map(int,sys.stdin.readline().split())
dic = {}
list = []

for idx in range(N):
    name = sys.stdin.readline().strip()
    dic[name] = idx+1
    list.append(name)

for _ in range(M):
    p = sys.stdin.readline().strip()

    if ord('0') <= ord(p[0]) <= ord('9'):
        print( list[int(p)-1] )

    elif ord('A') <= ord(p[0]) <= ord('Z'):
        print(dic[p])
