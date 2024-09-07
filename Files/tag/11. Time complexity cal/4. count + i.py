#a,b = map(int,sys.stdin.readline().split())

from array import array

import collections
import sys

n = int(sys.stdin.readline())

count = 0

for i in range(1,n):
    count += i

print(count)
print(2)