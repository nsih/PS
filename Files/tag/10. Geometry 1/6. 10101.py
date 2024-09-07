#a,b = map(int,sys.stdin.readline().split())

from array import array

import collections
import sys

angle = []

for _ in range(3):
    angle.append(int(sys.stdin.readline()))

if angle[0]+angle[1]+angle[2] != 180:
    print("Error")

else:
    if angle[0]==angle[1]==angle[2]:
        print("Equilateral")

    elif angle[0]==angle[1] or angle[1]==angle[2] or angle[0]==angle[2]:
        print("Isosceles")

    else:
        print("Scalene")