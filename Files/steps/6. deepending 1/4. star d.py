#sys.stdin.readline()

from array import array

a=int(input())
for i in range(1,a+1):
    print(' '*(a-i)+'*'*(2*i-1))
for i in range(1,a):
    print(' '*i+'*'*(2*a-2*i-1))

'''
import sys

n = int(sys.stdin.readline())

for i in range(n):
    for _ in range(n-(i+1) ):
        print(" ",end='')
    for j in range(n*2):
        if j < 1+(2*i):
            print("*",end='')
    print("")

for i in range(n-2,-1,-1):
    for _ in range(n-(i+1)):
        print(" ", end='')
    for j in range(n*2):
        if  j < (i*2)+1:
            print("*",end='')
    print("")
'''