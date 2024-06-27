import sys
import heapq

N = int(sys.stdin.readline())

absHeap = []
for _ in range(N):
    ip = int(sys.stdin.readline())

    if ip != 0:
        heapq.heappush(absHeap, (abs(ip),ip))

    else:
        if absHeap:
            print(heapq.heappop(absHeap)[1])
        else:
            print(0)