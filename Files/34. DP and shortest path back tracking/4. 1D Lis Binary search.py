import sys
import bisect

N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

lis = []

for i in range(N):
    pos = bisect.bisect_left(lis, lst[i])

    if pos < len(lis):
        lis[pos] = lst[i]
    else:
        lis.append(lst[i])

print(len(lis))