#a,b = map(int,sys.stdin.readline().split())

from array import array

import collections
import sys



while True:
    len = []
    len.clear()
    len = list(map(int,sys.stdin.readline().split()))

    len.sort()

    if len[0] == len[1] == len[2] == 0:
        break;

    elif len[0] + len[1] <= len[2]:
        print("Invalid")

    elif len[0] == len[1] == len[2]:
        print("Equilateral")

    elif len[0] == len[1] or len[1] == len[2] or len[0] == len[2]:
        print("Isosceles")

    else:
        print("Scalene")