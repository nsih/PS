#a,b = map(int,sys.stdin.readline().split())

from array import array

import sys

n = int(sys.stdin.readline())
count = n

p = []
p = map(int,sys.stdin.readline().split())

for item in p:
    if item == 1:
        count-=1
    else:
        for i in range(2,item):
            if item % i == 0:
                count -= 1
                break
print(count)