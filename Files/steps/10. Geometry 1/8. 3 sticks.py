#a,b = map(int,sys.stdin.readline().split())

from array import array

import collections
import sys

len = []
len = list(map(int,sys.stdin.readline().split()))
len.sort()

if len[0] + len[1] <= len[2]:
    len[2] = len[0] + len[1] - 1
    print(len[0] + len[1] + len[2])
else:
    print(len[0] + len[1] + len[2])
