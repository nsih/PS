import sys
import heapq

N = int(sys.stdin.readline())

maxHeap = []
for _ in range(N):
    ip = int(sys.stdin.readline())

    if ip > 0:
        heapq.heappush(maxHeap, ip)

    else:
        if maxHeap:
            print(heapq.heappop(maxHeap))
        else:
            print(0)