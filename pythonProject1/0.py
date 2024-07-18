def Dijkstra(start,end):
    dp = [INF] * (100000 + 1)
    dp[start] = 0

    Q = [(0, start)]

    while Q:
        time, pos = heapq.heappop(Q)

        # 이미 최소면 뜀
        if dp[pos] < time:
            continue

        # -1
        if pos - 1 >= 0:
            nextPos = pos-1
            nextTime = time+1

            if nextTime < dp[nextPos]:
                dp[nextPos] = nextTime
                heapq.heappush(Q, (nextTime, nextPos))
        # +1
        if pos + 1 <= 100000:
            nextPos = pos+1
            nextTime = time+1

            if nextTime < dp[nextPos]:
                dp[nextPos] = nextTime
                heapq.heappush(Q, (nextTime, nextPos))
        # *2
        if pos * 2 <= 100000:
            nextPos = pos*2
            nextTime = time

            if nextTime < dp[nextPos]:
                dp[nextPos] = nextTime
                heapq.heappush(Q, (nextTime, nextPos))

    return dp[end]


import sys
import heapq

INF = sys.maxsize
N, K = map(int, sys.stdin.readline().split())

print(Dijkstra(N,K))