#sys.stdin.readline()

import sys
n = int(sys.stdin.readline())

for i in range(1,n+1):
    for k in range(0, n-i):
        print(" ", end='')

    for j in range(0,i):
        if j != i-1:
            print("*",end='')
        else:
            print("*")