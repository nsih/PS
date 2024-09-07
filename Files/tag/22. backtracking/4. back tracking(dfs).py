import select
from array import array
import collections
import math
from functools import reduce
from collections import deque
import math
from collections import Counter
import sys

def DFS():
    if len(lst) == M:
        print(" ".join(map(str,lst)))
        return


    for i in range(1,N+1):
        if len(lst) == 0:
            lst.append(i)
            DFS()
            lst.pop()
        else:
            if i >= lst[-1]:
                lst.append(i)
                DFS()
                lst.pop()

N,M = map(int,sys.stdin.readline().split())

lst = []

DFS()