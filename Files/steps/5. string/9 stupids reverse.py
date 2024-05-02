#sys.stdin.readline()

from array import array
import sys

a, b = map(str, sys.stdin.readline().strip().split())

a = ''.join(reversed(a))
b = ''.join(reversed(b))

if int(a)>int(b):
    print(a)
else:
    print(b)