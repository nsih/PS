#sys.stdin.readline()

import sys
T = int(input())
for i in range(T):
        a,b = map(int, sys.stdin.readline().split())
        print("Case #"+str(i+1)+": "+str(a)+" + "+str(b)+" = "+str(a+b))