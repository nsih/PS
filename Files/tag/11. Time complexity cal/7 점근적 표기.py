#a,b = map(int,sys.stdin.readline().split())

from array import array

import collections
import sys

a0,a1 = map(int,sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

if c*n0 >= (a0*n0)+a1 and a0 <= c:
    print(1)
else:
    print(0)
