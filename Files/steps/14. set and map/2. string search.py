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
arr = []
for _ in range(N):
    dic[sys.stdin.readline().strip()] = 0

count = 0
for _ in range(M):
    if sys.stdin.readline().strip() in dic:
        count += 1

print(count)