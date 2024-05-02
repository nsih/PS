#sys.stdin.readline()

from array import array

import sys

A,B,V = map(int,sys.stdin.readline().split())

day = 0

if V <= A:
    day = 1

else:
    if ((V - A) % (A - B)) == 0 :
        day = ((V - A) // (A - B)) + 1
    else:
        day = ((V - A) // (A - B)) + 2

print(day)