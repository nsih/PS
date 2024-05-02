#sys.stdin.readline()

from array import array
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    st = sys.stdin.readline().strip()
    print(st[0] + st[-1])