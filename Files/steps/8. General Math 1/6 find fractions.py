#sys.stdin.readline()

from array import array

import sys

N = int(sys.stdin.readline().strip())

tempN = N
sum = 0
count = 0

while True:
    count += 1
    if N - count > 0:
        N = N-count
        sum = sum+count

    else:
        break;

#print(count,N)

if count % 2 == 0:
    print(N, end='')
    print("/",end='')
    print(count-(N-1),end='')
else:
    print(count-(N-1),end='')
    print("/", end='')
    print(N, end='')