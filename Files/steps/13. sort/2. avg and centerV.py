#a,b = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
from array import array
import collections
import sys
arr = []

for _ in range(5):
    arr.append(int(sys.stdin.readline()))

arr.sort()

print(sum(arr)//len(arr))
print(arr[2])