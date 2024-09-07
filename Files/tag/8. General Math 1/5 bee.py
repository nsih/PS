#sys.stdin.readline()

from array import array

import sys

N = int(sys.stdin.readline().strip())
count = 1

if N == 1:
    #print(N, count)
    print(1)

else:
    N = N-1
    while True:
        #print(N/6, count)
        if N/6 > count:
            N = N-(6*count)
            count += 1

        else:
            count += 1
            print(count)
            break;
