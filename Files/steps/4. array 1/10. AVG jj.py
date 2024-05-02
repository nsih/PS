#sys.stdin.readline()

from array import array
import sys


N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

max = max(arr)

for idx in range(N):
    arr[idx] = arr[idx]/max*100

print( sum(arr)/len(arr)  )