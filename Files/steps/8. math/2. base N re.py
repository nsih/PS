#sys.stdin.readline()

from array import array

import sys

N,B = map(int, sys.stdin.readline().strip().split())
result = []
while True:
    if N == 0:
        result.append(0)
        break;
    else:
        if N//B < B:
            result.append(N % B)
            if N // B > 0:
                result.append(N // B)
            N = N // B
            break;
        else:
            result.append(N % B)
            N = N // B

result = result[::-1]

for item in result:
    if item > 9:
        print(chr(item + ord("A")-10),end='')
    else:
        print(item,end='')