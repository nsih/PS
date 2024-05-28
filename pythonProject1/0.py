import select
from array import array
import collections
import math
from functools import reduce
from collections import deque
import math
from collections import Counter
import sys

def hanoi(N,a,b,c):
    if N == 1:
        print(a,c)
        return

    hanoi(N-1, a, c, b)
    print(a, c)
    hanoi(N-1, b, a, c)

N = int(sys.stdin.readline())
print((2**N)-1)
hanoi(N,1,2,3)

