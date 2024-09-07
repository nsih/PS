#sys.stdin.readline()

from array import array

import sys

N,B = map(str, sys.stdin.readline().strip().split())
B = int(B)

result = 0
leng = len(N)-1

for item in N:
    if ord(item) > 64:
        result += ((ord(item)-ord("A")+10) * B**leng)
        leng-=1
    else:
        result += (int(item) * B ** leng)
        leng -= 1


print(result,end='')