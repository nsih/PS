def Dijkstra(start):
    dp = [(INF,0)] * (start + 1)   #시간, 전 노드
    dp[start] = (0,0)

    Q = [(0, start)]

    while Q:
        time, pos = heapq.heappop(Q)

        # 이미 최소면 뜀
        if dp[pos][0] < time:
            continue

        # -1
        if pos % 3 == 0:
            nextPos = pos // 3
            nextTime = time+1

            if nextTime < dp[nextPos][0]:
                dp[nextPos] = (nextTime,pos)
                heapq.heappush(Q, (nextTime, nextPos))
        # +1
        if pos % 2 == 0:
            nextPos = pos // 2
            nextTime = time+1

            if nextTime < dp[nextPos][0]:
                dp[nextPos] = (nextTime, pos)
                heapq.heappush(Q, (nextTime, nextPos))
        # *2
        if pos - 1 >= 1:
            nextPos = pos-1
            nextTime = time+1

            if nextTime < dp[nextPos][0]:
                dp[nextPos] = (nextTime, pos)
                heapq.heappush(Q, (nextTime, nextPos))

    path = []
    path.append(1)
    s = 1
    while dp[s][1]:
        path.append(dp[s][1])
        s = dp[s][1]
    path.reverse()

    print(dp[1][0])

    return path


import sys
import heapq

INF = sys.maxsize
N = int(sys.stdin.readline())

print(*Dijkstra(N))