#a,b = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
#arr.sort(key=lambda x: (len(x),ord(x[0])))
#iDict = {value: index for index, value in enumerate(arr)}

from array import array
import collections
import sys
N = int(sys.stdin.readline())
dic = {}
list = []
for _ in range(N):
    a, b = map(str, sys.stdin.readline().split())
    if b == "enter":
        dic[a] = 1
    elif b == "leave":
        dic[a] = 0
for i in dic:
    if dic[i] == 1:
        list.append(i)
list.sort(reverse=True)
for i in list:
    print(i)
