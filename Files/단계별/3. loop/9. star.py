#sys.stdin.readline()

import sys
T = int(sys.stdin.readline())
for i in range(0,T+1):
        for j in range(0,i):
            if j != i-1:
                print("*",end='')
            else:
                print("*")