def Dijkstra(start):
    dp = [INF] * (N + 1)
    dp[start] = 0
    heap = []
    heapq.heappush(heap,(0, start))

    while heap:
        #가중치 정점
        wei, now = heapq.heappop(heap)

        #더 짧은거 있으면 그냥 넘어감
        if dp[now] < wei:
            continue

        #현재 정점의 간선 순회
        for dw, du in graph[now]:
            nextWei = dw + wei
            if nextWei < dp[du]:   #최소거리를 찾으면 적용
                dp[du] = nextWei
                heapq.heappush(heap,(nextWei,du))

    return dp


import sys
import heapq

INF = sys.maxsize
N, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]


for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

v1,v2 = map(int, sys.stdin.readline().split())

dp = Dijkstra(1)
dp2 = Dijkstra(v1)
dp3 = Dijkstra(v2)

r1 = dp[v1] + dp2[v2] + dp3[N]
r2 = dp[v2] + dp3[v1] + dp2[N]

r = min(r1,r2)

if r >= INF:
    print(-1)
else:
    print(r)