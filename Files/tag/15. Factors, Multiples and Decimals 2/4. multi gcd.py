#N,M = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
#arr.sort(key=lambda x: (len(x),ord(x[0])))
#iDict = {value: index for index, value in enumerate(arr)}

from array import array
import collections
import math
from functools import reduce
import math
from functools import reduce
import sys
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
N = int(sys.stdin.readline())
grs = []
dist = []
rDist = 0
for i in range(N):
    grs.append(int(sys.stdin.readline()))
    if i == 1:
        rDist = grs[i]-grs[i-1]
    elif i > 1:
        rDist = gcd(rDist, grs[i]-grs[i-1])
print ((((max(grs)-min(grs)) // rDist )+1)-len(grs))