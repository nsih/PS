#sys.stdin.readline()

from array import array
import sys

a,X = map(int, sys.stdin.readline().split())
list = list(map(int, sys.stdin.readline().split()))

for i in list:
    if i < X:
        print(i,end=' ')