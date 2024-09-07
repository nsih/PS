#a,b = map(int,sys.stdin.readline().split())

from array import array

import sys
import collections

x = []
y = []
for _ in range(3):
    a, b = map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)

xCounts = collections.Counter(x)
yCounts = collections.Counter(y)

print(min(xCounts, key=xCounts.get), min(yCounts, key=yCounts.get))



'''
x = []
y = []
for _ in range(3):
    a, b = map(int, sys.stdin.readline().split())
    if x.__contains__(a):
        x.remove(a)
    else:
        x.append(a)

    if y.__contains__(b):
        y.remove(b)
    else:
        y.append(b)

print(x[0],y[0])
'''