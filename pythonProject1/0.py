#N,M = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
#arr.sort(key=lambda x: (len(x),ord(x[0])))
#iDict = {value: index for index, value in enumerate(arr)}

from array import array
import collections
import sys
N = int(sys.stdin.readline().strip())
count = N
for i in range(N):
    seq = sys.stdin.readline().strip()
    for idx in range(len(seq)-1):
        if seq[idx] == "C" and seq[idx+1] == "D":
            count -= 1
print(count)