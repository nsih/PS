#a,b = map(int,sys.stdin.readline().split())

from array import array

import collections
import sys

x = []
y = []
n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)

print((max(x)-min(x)) * (max(y)-min(y)))