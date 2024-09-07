#sys.stdin.readline()

from array import array
import sys

n = sys.stdin.readline()
st = sys.stdin.readline().strip()

sum = 0
for i in range(len(st)):
    sum += int(st[i])

print(sum)