#sys.stdin.readline()

from array import array
import sys

arr = []

for i in range(10):
    a = int(sys.stdin.readline()) % 42
    if a in arr:
        continue
    else:
        arr.append(a)

print(len(arr))