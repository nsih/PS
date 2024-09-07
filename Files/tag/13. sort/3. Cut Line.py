#a,b = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
from array import array
import collections
import sys
N,k = map(int,sys.stdin.readline().split())

arr = []
arr = list(map(int,sys.stdin.readline().split()))


arr.sort(reverse=True)
print(arr[k-1])