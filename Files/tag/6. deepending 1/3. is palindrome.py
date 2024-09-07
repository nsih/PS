#sys.stdin.readline()

from array import array
import sys

arr = sys.stdin.readline().strip()

if arr == ''.join(reversed(arr)):
    print(1)
else:
    print(0)